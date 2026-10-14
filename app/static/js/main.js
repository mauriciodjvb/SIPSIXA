// JavaScript global de SIPSIXA.
document.addEventListener("DOMContentLoaded", () => {
    // Menú móvil (hamburguesa)
    const toggle = document.querySelector("[data-nav-toggle]");
    const nav = document.querySelector("[data-nav]");

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            const abierto = nav.classList.toggle("is-open");
            toggle.setAttribute("aria-expanded", String(abierto));
        });

        // cerrar el menú al elegir una sección
        nav.querySelectorAll("a").forEach((enlace) => {
            enlace.addEventListener("click", () => {
                nav.classList.remove("is-open");
                toggle.setAttribute("aria-expanded", "false");
            });
        });
    }
});
