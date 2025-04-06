document.addEventListener("DOMContentLoaded", function () {
    // Inicializar tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Función para activar el modo pantalla completa
    function toggleFullScreen(video) {
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.mozRequestFullScreen) { // Firefox
            video.mozRequestFullScreen();
        } else if (video.webkitRequestFullscreen) { // Chrome, Safari y Opera
            video.webkitRequestFullscreen();
        } else if (video.msRequestFullscreen) { // IE/Edge
            video.msRequestFullscreen();
        }
    }

    // Mostrar PDF o Video en modal
    function showModal(event) {
        const contentUrl = this.getAttribute("data-pdf") || this.getAttribute("data-video");

        // Comprobar si la URL contiene "mpl-game-presentation" o si el archivo es PDF o MP4
        if (!contentUrl || 
            (!contentUrl.endsWith(".pdf") && !contentUrl.endsWith(".mp4") && !contentUrl.includes("mpl-game-presentation"))) {
            return; // No hacer nada si no es ni PDF, ni MP4, ni contiene "mpl-game-presentation"
        }

        const isVideo = contentUrl.endsWith(".mp4");

        const modalContent = document.getElementById("modalContent");
        modalContent.innerHTML = "";

        if (isVideo) {
            const video = document.createElement("video");
            video.src = contentUrl;
            video.id = "myVideo";
            video.style.width = "100%";
            video.style.maxHeight = "800px";
            video.style.cursor = "pointer";
            video.setAttribute("muted", "");
            video.setAttribute("playsinline", "");
            video.addEventListener("click", function () {
                video.currentTime = 0;
                video.play();
            });
            
            // Agregar evento para doble clic en el video (pantalla completa)
            video.addEventListener("dblclick", function () {
                toggleFullScreen(video);
            });

            modalContent.appendChild(video);
        } else {
            const iframe = document.createElement("iframe");
            iframe.src = contentUrl;
            iframe.style.width = "100%";
            iframe.style.height = "800px";
            iframe.setAttribute("frameborder", "0");
            modalContent.appendChild(iframe);
        }

        const auxModal = new bootstrap.Modal(document.getElementById("auxModal"));
        auxModal.show();
    }

    // Asignar eventos a los elementos con clase multimedia
    document.querySelectorAll(".curriculum-icon, .education-icon, .project-image").forEach(function (element) {
        element.addEventListener("click", showModal);
    });

    // Pausar y limpiar el contenido al cerrar el modal o hacer clic fuera del modal
    function closeModal() {
        const modalContent = document.getElementById("modalContent");
        const video = modalContent.querySelector("video");
        if (video) {
            video.pause();
            video.currentTime = 0;
        }
        modalContent.innerHTML = "";
    }

    // Evento de cierre del modal
    var modal = document.getElementById("auxModal");
    modal.addEventListener("hidden.bs.modal", closeModal);

    // Cerrar el modal al hacer clic fuera de él (si se hace clic en el fondo)
    modal.addEventListener("click", function (e) {
        if (e.target === modal) {
            const bootstrapModal = new bootstrap.Modal(modal);
            bootstrapModal.hide();
        }
    });

    // Reproducir automáticamente el video cuando se abra el modal
    modal.addEventListener("shown.bs.modal", function () {
        const video = document.getElementById("myVideo");
        if (video) {
            video.currentTime = 0;
            video.play();
        }
    });

    // Mostrar el año actual en el footer
    const yearSpan = document.createElement("span");
    yearSpan.textContent = new Date().getFullYear();
    const aboutTitle = document.querySelector(".about-tittle p");
    if (aboutTitle) {
        aboutTitle.appendChild(yearSpan);
    }
});
