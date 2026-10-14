/* ==========================================================================
   Lógica de las pantallas con sesión: login, dashboard, registrar contenido,
   validación (administrador) e indicadores. Es un prototipo: los datos viven
   en el navegador (ver sesion.js).
   ========================================================================== */
(() => {
    const ICONOS = { Proyecto: "💡", Premio: "🏆", Evento: "📅", "Investigación": "🔬", "Hall de la Fama": "⭐", Historia: "🕰️" };
    const ETIQUETAS = { pendiente: "Pendiente", aprobado: "Aprobado", rechazado: "Rechazado" };

    // Siempre se construye el HTML con textContent: lo que escribe el usuario nunca se interpreta como código.
    function crear(etiqueta, clase, texto) {
        const el = document.createElement(etiqueta);
        if (clase) el.className = clase;
        if (texto !== undefined) el.textContent = texto;
        return el;
    }
    const poner = (selector, valor) =>
        document.querySelectorAll(selector).forEach((el) => { el.textContent = String(valor); });
    const estadoValido = (e) => (ETIQUETAS[e] ? e : "pendiente");
    const pendientes = () => Sipsixa.contenidos().filter((c) => c.estado === "pendiente");

    function mostrarVacio(contenedor, texto) {
        contenedor.append(crear("div", "fila fila--vacia", texto));
    }

    /* ---------------------------- LOGIN / REGISTRO ---------------------------- */
    function destinoSeguro(ruta) {
        return ruta && ruta.startsWith("/") && !ruta.startsWith("//") ? ruta : "/dashboard";
    }

    function iniciarLogin() {
        const params = new URLSearchParams(location.search);
        const botones = [...document.querySelectorAll("[data-modo]")];
        const formularios = [...document.querySelectorAll("[data-form]")];

        function cambiarModo(modo) {
            botones.forEach((b) => {
                const activo = b.dataset.modo === modo;
                b.classList.toggle("is-active", activo);
                b.setAttribute("aria-selected", String(activo));
            });
            formularios.forEach((f) => { f.hidden = f.dataset.form !== modo; });
        }
        botones.forEach((b) => b.addEventListener("click", () => cambiarModo(b.dataset.modo)));
        cambiarModo(params.get("modo") === "registro" ? "registro" : "login");

        formularios.forEach((form) => {
            const error = form.querySelector("[data-error]");
            form.addEventListener("submit", (e) => {
                e.preventDefault();
                error.hidden = true;

                if (!form.checkValidity()) {
                    const campo = form.querySelector(":invalid");
                    error.textContent = campo.validationMessage || "Revisa los campos del formulario.";
                    if (campo.getAttribute("title") && campo.validity.patternMismatch) error.textContent = campo.title;
                    error.hidden = false;
                    campo.focus();
                    return;
                }

                const datos = new FormData(form);
                const correo = String(datos.get("correo")).trim().toLowerCase();
                const esRegistro = form.dataset.form === "registro";
                const rol = esRegistro ? String(datos.get("rol")) : Sipsixa.rolPorCorreo(correo);
                const usuario = {
                    nombre: esRegistro ? String(datos.get("nombre")).trim() : Sipsixa.nombreDesdeCorreo(correo),
                    correo,
                    rol: Sipsixa.ROLES[rol] ? rol : "estudiante",
                };

                const boton = form.querySelector("button[type=submit]");
                boton.disabled = true;
                boton.textContent = esRegistro ? "Creando cuenta..." : "Ingresando...";
                setTimeout(() => {
                    Sipsixa.iniciarSesion(usuario);
                    location.href = destinoSeguro(params.get("siguiente"));
                }, 700);
            });
        });
    }

    /* -------------------------------- DASHBOARD -------------------------------- */
    function filaPropuesta(c) {
        const estado = estadoValido(c.estado);
        const fila = crear("div", "fila");
        const cuerpo = crear("div", "fila__cuerpo");
        cuerpo.append(
            crear("p", "fila__titulo", c.titulo),
            crear("p", "fila__meta", `${c.tipo} · ${Sipsixa.formatoFecha(c.fecha)}`)
        );
        if (estado === "rechazado" && c.observaciones) {
            cuerpo.append(crear("p", "fila__obs", "Observaciones: " + c.observaciones));
        }
        fila.append(crear("div", "fila__icono", ICONOS[c.tipo] || "📄"), cuerpo, crear("span", "estado estado--" + estado, ETIQUETAS[estado]));
        return fila;
    }

    function iniciarDashboard() {
        const u = Sipsixa.usuario();
        Sipsixa.asegurarPropuestasDemo(u);

        const mias = Sipsixa.contenidos().filter((c) => c.autorCorreo === u.correo).sort((a, b) => b.id - a.id);
        const notifs = Sipsixa.notificaciones().filter((n) => n.correo === u.correo);

        poner("[data-n-aportes]", mias.length);
        poner("[data-n-notif]", notifs.length);
        poner("[data-n-pendientes]", pendientes().length);

        const listaMias = document.querySelector("[data-mis-propuestas]");
        mias.forEach((c) => listaMias.append(filaPropuesta(c)));
        if (!mias.length) mostrarVacio(listaMias, "Aún no has enviado propuestas.");

        const listaNotifs = document.querySelector("[data-notificaciones]");
        notifs.slice(0, 6).forEach((n) => {
            const fila = crear("div", "fila");
            const cuerpo = crear("div", "fila__cuerpo");
            cuerpo.append(crear("p", "fila__titulo", n.mensaje), crear("p", "fila__meta", Sipsixa.formatoFecha(n.fecha)));
            fila.append(crear("div", "fila__icono", n.icono || "🔔"), cuerpo);
            listaNotifs.append(fila);
        });
        if (!notifs.length) mostrarVacio(listaNotifs, "No tienes notificaciones.");
    }

    /* ------------------------------ REGISTRAR CONTENIDO ------------------------------ */
    const MAX_BYTES = 10 * 1024 * 1024;
    const TIPOS_OK = ["image/png", "image/jpeg", "application/pdf"];

    const tamano = (bytes) => (bytes < 1048576 ? Math.round(bytes / 1024) + " KB" : (bytes / 1048576).toFixed(1) + " MB");

    function iniciarRegistrar() {
        const form = document.querySelector("[data-form-contenido]");
        const error = form.querySelector("[data-error]");
        const entrada = form.querySelector("input[type=file]");
        const zona = form.querySelector("[data-dropzone]");
        const lista = form.querySelector("[data-archivos]");

        function mostrarArchivos() {
            lista.replaceChildren();
            [...entrada.files].forEach((a) => {
                const li = crear("li");
                li.append(crear("span", "", a.name), crear("span", "", tamano(a.size)));
                lista.append(li);
            });
        }
        function archivosValidos() {
            return [...entrada.files].every((a) => a.size <= MAX_BYTES && TIPOS_OK.includes(a.type));
        }

        entrada.addEventListener("change", mostrarArchivos);
        ["dragenter", "dragover"].forEach((ev) => zona.addEventListener(ev, (e) => { e.preventDefault(); zona.classList.add("is-over"); }));
        ["dragleave", "drop"].forEach((ev) => zona.addEventListener(ev, (e) => { e.preventDefault(); zona.classList.remove("is-over"); }));
        zona.addEventListener("drop", (e) => {
            if (e.dataTransfer && e.dataTransfer.files.length) {
                entrada.files = e.dataTransfer.files;
                mostrarArchivos();
            }
        });

        form.addEventListener("submit", (e) => {
            e.preventDefault();
            error.hidden = true;
            form.querySelectorAll(".is-invalid").forEach((c) => c.classList.remove("is-invalid"));

            const invalido = form.querySelector(":invalid:not([type=file])");
            if (invalido) {
                invalido.classList.add("is-invalid");
                error.textContent = "Completa los campos obligatorios: " + (invalido.validationMessage || "revisa el valor ingresado.");
                error.hidden = false;
                invalido.focus();
                return;
            }
            if (!archivosValidos()) {
                error.textContent = "Las evidencias deben ser PNG, JPG o PDF de máximo 10 MB cada una.";
                error.hidden = false;
                return;
            }

            const u = Sipsixa.usuario();
            const datos = new FormData(form);
            const lista_ = Sipsixa.contenidos();
            lista_.push({
                id: Date.now(),
                tipo: String(datos.get("categoria")),
                titulo: String(datos.get("titulo")).trim(),
                autor: u.nombre,
                autorCorreo: u.correo,
                fecha: new Date().toISOString().slice(0, 10),
                estado: "pendiente",
                observaciones: "",
            });
            Sipsixa.guardarContenidos(lista_);

            const boton = form.querySelector("button[type=submit]");
            boton.disabled = true;
            boton.textContent = "Enviando...";
            setTimeout(() => {
                document.querySelector("[data-formulario]").hidden = true;
                document.querySelector("[data-exito]").hidden = false;
                window.scrollTo({ top: 0 });
            }, 600);
        });
    }

    /* --------------------------------- VALIDACIÓN --------------------------------- */
    let temporizadorToast;
    function toast(mensaje, tipo) {
        const el = document.querySelector("[data-toast]");
        el.textContent = mensaje;
        el.className = "toast toast--" + tipo;
        el.hidden = false;
        clearTimeout(temporizadorToast);
        temporizadorToast = setTimeout(() => { el.hidden = true; }, 3500);
    }

    function resolver(id, estado, observaciones) {
        const todos = Sipsixa.contenidos();
        const c = todos.find((x) => x.id === id);
        if (!c) return;
        c.estado = estado;
        c.observaciones = observaciones;
        Sipsixa.guardarContenidos(todos);

        if (estado === "aprobado") {
            Sipsixa.notificar(c.autorCorreo, `Tu aporte «${c.titulo}» fue aprobado y publicado.`, "✅");
            toast("Contenido aprobado. Se notificó al autor.", "ok");
        } else {
            Sipsixa.notificar(c.autorCorreo, `Tu aporte «${c.titulo}» fue devuelto con observaciones: ${observaciones}`, "↩️");
            toast("Contenido devuelto con observaciones. Se notificó al autor.", "aviso");
        }
    }

    function tarjetaValidacion(c, repintar) {
        const tarjeta = crear("article", "card validar__item");

        const cab = crear("div", "validar__cab");
        const cuerpo = crear("div", "fila__cuerpo");
        cuerpo.append(
            crear("span", "badge", c.tipo),
            crear("h3", "", c.titulo),
            crear("p", "fila__meta", `Por ${c.autor} · ${Sipsixa.formatoFecha(c.fecha)}`)
        );
        cab.append(crear("div", "fila__icono", ICONOS[c.tipo] || "📄"), cuerpo, crear("span", "estado estado--pendiente", "Pendiente"));

        const acciones = crear("div", "validar__acciones");
        const aprobar = crear("button", "btn btn--verde", "✓ Aprobar");
        const devolver = crear("button", "btn btn--borde", "↩ Devolver con observaciones");
        aprobar.type = devolver.type = "button";
        acciones.append(aprobar, devolver);

        const rechazo = crear("div", "validar__rechazo");
        rechazo.hidden = true;
        const area = crear("textarea", "input input--area");
        area.rows = 3;
        area.placeholder = "Escribe las observaciones para el autor...";
        area.setAttribute("aria-label", "Observaciones para el autor");
        const aviso = crear("p", "form-error", "Escribe al menos una observación para poder devolver el contenido.");
        aviso.hidden = true;
        const enviar = crear("button", "btn btn--red", "Enviar observaciones");
        enviar.type = "button";
        rechazo.append(area, aviso, enviar);

        aprobar.addEventListener("click", () => { resolver(c.id, "aprobado", ""); repintar(); });
        devolver.addEventListener("click", () => { rechazo.hidden = !rechazo.hidden; if (!rechazo.hidden) area.focus(); });
        enviar.addEventListener("click", () => {
            const texto = area.value.trim();
            if (!texto) { aviso.hidden = false; area.classList.add("is-invalid"); area.focus(); return; }
            resolver(c.id, "rechazado", texto);
            repintar();
        });

        tarjeta.append(cab, acciones, rechazo);
        return tarjeta;
    }

    function iniciarValidacion() {
        const contenedor = document.querySelector("[data-lista]");
        const vacio = document.querySelector("[data-vacio]");

        function repintar() {
            contenedor.replaceChildren();
            const lista = pendientes();
            lista.forEach((c) => contenedor.append(tarjetaValidacion(c, repintar)));
            vacio.hidden = lista.length > 0;
        }
        repintar();
    }

    /* --------------------------------- INDICADORES --------------------------------- */
    function iniciarIndicadores() {
        const contenedor = document.querySelector("[data-pendientes]");
        const lista = pendientes();
        lista.slice(0, 4).forEach((c) => {
            const fila = crear("div", "fila");
            const cuerpo = crear("div", "fila__cuerpo");
            cuerpo.append(crear("p", "fila__titulo", c.titulo), crear("p", "fila__meta", `${c.tipo} · ${c.autor}`));
            fila.append(crear("div", "fila__icono", ICONOS[c.tipo] || "📄"), cuerpo, crear("span", "estado estado--pendiente", "Pendiente"));
            contenedor.append(fila);
        });
        if (!lista.length) mostrarVacio(contenedor, "No hay aportes pendientes.");
    }

    /* ------------------------------------ INICIO ------------------------------------ */
    const paginas = {
        login: iniciarLogin,
        dashboard: iniciarDashboard,
        registrar: iniciarRegistrar,
        validacion: iniciarValidacion,
        indicadores: iniciarIndicadores,
    };

    document.addEventListener("DOMContentLoaded", () => {
        const pagina = document.body.dataset.pagina;
        const requiere = document.body.dataset.requiere;
        // en páginas protegidas, solo se ejecuta si sesion.js dejó pasar al usuario
        if (requiere && !document.body.classList.contains("auth-ok")) return;
        if (paginas[pagina]) paginas[pagina]();
    });
})();
