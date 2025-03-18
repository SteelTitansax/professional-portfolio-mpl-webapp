document.addEventListener("DOMContentLoaded", function () {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // show pdfs modal 
    function showModal(event) {
        let pdfUrl = this.getAttribute("data-pdf");
        if (pdfUrl) {
            document.getElementById("pdfViewer").src = pdfUrl;
            let auxModal = new bootstrap.Modal(document.getElementById("auxModal"));
            auxModal.show();
        }
    }

    // Asign events with class elements curriculum-icon and education-icon
    document.querySelectorAll(".curriculum-icon, .education-icon, .project-image").forEach(function (element) {
        element.addEventListener("click", showModal);
    });

    // Clean iframe when closing modal
    var modal = document.getElementById("auxModal");
    modal.addEventListener("hidden.bs.modal", function () {
        var iframe = modal.querySelector("iframe");
        if (iframe) {
            iframe.src = ""; // Clean src 
        }
    });

    // Show actual year in footer
    var yearSpan = document.createElement("span");
    yearSpan.textContent = new Date().getFullYear();
    document.querySelector(".little-text p").appendChild(yearSpan);
});