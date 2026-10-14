// JavaScript global de SIPSIXA.

// Quita tildes y pasa a minúsculas para que la búsqueda no distinga "Sofía" de "sofia".
const normalizar = (texto) =>
    (texto || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().trim();

/* ---------- Menú móvil (hamburguesa) ---------- */
function iniciarMenu() {
    const boton = document.querySelector("[data-nav-toggle]");
    const nav = document.querySelector("[data-nav]");
    if (!boton || !nav) return;

    boton.addEventListener("click", () => {
        const abierto = nav.classList.toggle("is-open");
        boton.setAttribute("aria-expanded", String(abierto));
    });
    nav.querySelectorAll("a").forEach((enlace) =>
        enlace.addEventListener("click", () => {
            nav.classList.remove("is-open");
            boton.setAttribute("aria-expanded", "false");
        })
    );
}

/* ---------- Listados con filtros y buscador ----------
   <div data-listado>
     <div data-filtro="anio"> <button data-valor="2024"> ... </div>
     <input data-buscar>
     <a data-item data-anio="2024" data-texto="..."> ... </a>
     <p data-vacio hidden>
*/
function iniciarListado(zona) {
    const items = [...zona.querySelectorAll("[data-item]")];
    const grupos = [...zona.querySelectorAll("[data-filtro]")];
    const buscador = zona.querySelector("[data-buscar]");
    const vacio = zona.querySelector("[data-vacio]");
    const estado = {};

    function aplicar() {
        const consulta = normalizar(buscador ? buscador.value : "");
        let visibles = 0;

        items.forEach((item) => {
            let coincide = Object.entries(estado).every(
                ([clave, valor]) => valor === "Todos" || item.dataset[clave] === valor
            );
            if (coincide && consulta && !normalizar(item.dataset.texto).includes(consulta)) {
                coincide = false;
            }
            item.hidden = !coincide;
            if (coincide) visibles += 1;
        });

        if (vacio) vacio.hidden = visibles > 0;
    }

    grupos.forEach((grupo) => {
        const botones = [...grupo.querySelectorAll("[data-valor]")];
        const inicial = botones.find((b) => b.classList.contains("is-active"));
        estado[grupo.dataset.filtro] = inicial ? inicial.dataset.valor : "Todos";

        botones.forEach((boton) =>
            boton.addEventListener("click", () => {
                estado[grupo.dataset.filtro] = boton.dataset.valor;
                botones.forEach((b) => b.classList.toggle("is-active", b === boton));
                aplicar();
            })
        );
    });

    if (buscador) buscador.addEventListener("input", aplicar);
    aplicar();
}

/* ---------- Historia: línea de tiempo con panel de detalle ---------- */
function iniciarLineaTiempo(zona) {
    const items = [...zona.querySelectorAll(".timeline__item")];
    const panel = zona.querySelector("[data-panel]");
    const vacio = zona.querySelector("[data-panel-vacio]");
    let seleccionado = null;

    function mostrar(item) {
        items.forEach((i) => i.classList.toggle("is-selected", i === item));
        seleccionado = item;

        if (!item) {
            panel.hidden = true;
            vacio.hidden = false;
            return;
        }
        const d = item.dataset;
        panel.querySelector("[data-p-img]").src = d.img;
        panel.querySelector("[data-p-img]").alt = d.titulo;
        panel.querySelector("[data-p-fecha]").textContent = d.fecha;
        panel.querySelector("[data-p-titulo]").textContent = d.titulo;
        panel.querySelector("[data-p-desc]").textContent = d.desc;
        panel.querySelector("[data-p-anio]").textContent = d.anio;
        panel.hidden = false;
        vacio.hidden = true;
    }

    items.forEach((item) => {
        const tarjeta = item.querySelector(".timeline__card");
        const alternar = () => mostrar(seleccionado === item ? null : item);
        tarjeta.addEventListener("click", alternar);
        tarjeta.addEventListener("keydown", (e) => {
            if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                alternar();
            }
        });
    });
}

/* ---------- Ventanas emergentes (<dialog>) ---------- */
function iniciarModales() {
    document.querySelectorAll("[data-abrir]").forEach((boton) =>
        boton.addEventListener("click", () => {
            const ventana = document.getElementById(boton.dataset.abrir);
            if (ventana && ventana.showModal) ventana.showModal();
        })
    );
    document.querySelectorAll("dialog").forEach((ventana) => {
        ventana.querySelectorAll("[data-cerrar]").forEach((b) =>
            b.addEventListener("click", () => ventana.close())
        );
        // clic fuera de la ventana = cerrar
        ventana.addEventListener("click", (e) => {
            if (e.target === ventana) ventana.close();
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    iniciarMenu();
    document.querySelectorAll("[data-listado]").forEach(iniciarListado);
    document.querySelectorAll("[data-linea]").forEach(iniciarLineaTiempo);
    iniciarModales();
});
