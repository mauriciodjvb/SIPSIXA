/* ==========================================================================
   Sesión de demostración y datos guardados en el navegador.
   Es un prototipo: NO hay contraseñas reales. En la fase 3 se reemplaza por
   el login con JWT y la base de datos.
   ========================================================================== */
const Sipsixa = (() => {
    const CLAVES = {
        usuario: "sipsixa_usuario",
        contenidos: "sipsixa_contenidos",
        notificaciones: "sipsixa_notificaciones",
    };
    const ROLES = { estudiante: "Estudiante", docente: "Docente", egresado: "Egresado", administrador: "Administrador" };

    /* ----- almacenamiento (con protección si el navegador lo bloquea) ----- */
    function leer(clave, porDefecto) {
        try {
            const valor = JSON.parse(localStorage.getItem(clave));
            return valor === null ? porDefecto : valor;
        } catch {
            return porDefecto;
        }
    }
    function guardar(clave, valor) {
        try { localStorage.setItem(clave, JSON.stringify(valor)); } catch { /* sin almacenamiento */ }
    }

    /* ----- usuario ----- */
    const usuario = () => leer(CLAVES.usuario, null);
    const iniciarSesion = (u) => guardar(CLAVES.usuario, u);
    function cerrarSesion() {
        try { localStorage.removeItem(CLAVES.usuario); } catch { /* nada */ }
    }

    function rolPorCorreo(correo) {
        const c = correo.toLowerCase();
        if (c.includes("admin")) return "administrador";
        if (c.includes("docente") || c.includes("prof")) return "docente";
        if (c.includes("egresado")) return "egresado";
        return "estudiante";
    }
    function nombreDesdeCorreo(correo) {
        const base = correo.split("@")[0].replace(/[._-]+/g, " ").trim();
        return base.replace(/\b\w/g, (l) => l.toUpperCase()) || "Usuario";
    }

    /* ----- contenidos propuestos (semilla + los que envía el usuario) ----- */
    function semilla() {
        const el = document.getElementById("semilla");
        try { return el ? JSON.parse(el.textContent) : []; } catch { return []; }
    }
    function contenidos() {
        let lista = leer(CLAVES.contenidos, null);
        if (!Array.isArray(lista)) {
            lista = semilla();
            guardar(CLAVES.contenidos, lista);
        }
        return lista;
    }
    const guardarContenidos = (lista) => guardar(CLAVES.contenidos, lista);

    /* ----- notificaciones ----- */
    const notificaciones = () => leer(CLAVES.notificaciones, []);
    function notificar(correo, mensaje, icono) {
        const lista = notificaciones();
        lista.unshift({ correo, mensaje, icono, fecha: new Date().toISOString() });
        guardar(CLAVES.notificaciones, lista.slice(0, 50));
    }

    // Primera vez que el usuario entra: se crean dos aportes de ejemplo para ver los estados.
    function asegurarPropuestasDemo(u) {
        const lista = contenidos();
        if (lista.some((c) => c.autorCorreo === u.correo)) return;
        const hoy = Date.now();
        lista.push(
            { id: hoy, tipo: "Proyecto", titulo: "EcoTracker – App de huella de carbono", autor: u.nombre, autorCorreo: u.correo,
              fecha: "2025-07-20", estado: "aprobado", observaciones: "" },
            { id: hoy + 1, tipo: "Evento", titulo: "Taller de Python para principiantes", autor: u.nombre, autorCorreo: u.correo,
              fecha: "2025-07-28", estado: "rechazado", observaciones: "Falta adjuntar evidencia fotográfica del evento." }
        );
        guardarContenidos(lista);
        notificar(u.correo, "Tu aporte «EcoTracker – App de huella de carbono» fue aprobado y publicado.", "✅");
        notificar(u.correo, "Tu aporte «Taller de Python para principiantes» fue devuelto con observaciones.", "↩️");
    }

    function formatoFecha(iso) {
        const fecha = new Date(iso.length === 10 ? iso + "T12:00:00" : iso);
        return fecha.toLocaleDateString("es-CO", { day: "numeric", month: "short", year: "numeric" });
    }

    /* ----- interfaz: barra superior y protección de páginas ----- */
    function pintar() {
        const u = usuario();

        document.querySelectorAll("[data-sesion]").forEach((el) => {
            el.hidden = el.dataset.sesion === "dentro" ? !u : Boolean(u);
        });
        document.querySelectorAll("[data-solo-admin]").forEach((el) => {
            el.hidden = !u || u.rol !== "administrador";
        });
        if (!u) return;

        const poner = (selector, texto) =>
            document.querySelectorAll(selector).forEach((el) => { el.textContent = texto; });
        poner("[data-u-nombre]", u.nombre);
        poner("[data-u-primer]", u.nombre.split(" ")[0]);
        poner("[data-u-inicial]", u.nombre.charAt(0).toUpperCase());
        poner("[data-u-rol]", ROLES[u.rol] || "Usuario");
    }

    function proteger() {
        const requiere = document.body.dataset.requiere;
        if (!requiere) return true;

        const u = usuario();
        if (!u) {
            location.replace("/login?siguiente=" + encodeURIComponent(location.pathname));
            return false;
        }
        if (requiere === "administrador" && u.rol !== "administrador") {
            location.replace("/dashboard");
            return false;
        }
        document.body.classList.add("auth-ok");
        return true;
    }

    function iniciarMenuUsuario() {
        const boton = document.querySelector("[data-menu-usuario]");
        const panel = document.querySelector("[data-menu-panel]");
        if (!boton || !panel) return;

        const cerrar = () => { panel.hidden = true; boton.setAttribute("aria-expanded", "false"); };
        boton.addEventListener("click", (e) => {
            e.stopPropagation();
            panel.hidden = !panel.hidden;
            boton.setAttribute("aria-expanded", String(!panel.hidden));
        });
        document.addEventListener("click", (e) => { if (!panel.contains(e.target)) cerrar(); });
        document.addEventListener("keydown", (e) => { if (e.key === "Escape") cerrar(); });

        document.querySelectorAll("[data-cerrar-sesion]").forEach((b) =>
            b.addEventListener("click", () => {
                cerrarSesion();
                location.href = "/";
            })
        );
    }

    document.addEventListener("DOMContentLoaded", () => {
        if (!proteger()) return;
        pintar();
        iniciarMenuUsuario();
    });

    return {
        ROLES, usuario, iniciarSesion, cerrarSesion, rolPorCorreo, nombreDesdeCorreo,
        contenidos, guardarContenidos, notificaciones, notificar, asegurarPropuestasDemo, formatoFecha,
    };
})();
