document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});


// Modals code 
// -------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    document.querySelectorAll(".curriculum-icon").forEach(function (element) {
        element.addEventListener("click", function () {
            let pdfUrl = this.getAttribute("data-pdf");
            document.getElementById("pdfViewer").src = pdfUrl;
            let auxModal = new bootstrap.Modal(document.getElementById("auxModal"));
            auxModal.show();
        });
    });
});



document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });

    document.querySelectorAll(".education-icon").forEach(function (element) {
        element.addEventListener("click", function () {
            let pdfUrl = this.getAttribute("data-pdf");
            document.getElementById("pdfViewer").src = pdfUrl;
            let auxModal = new bootstrap.Modal(document.getElementById("auxModal"));
            auxModal.show();
        });
    });

document.addEventListener("DOMContentLoaded", function () {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.forEach(function (tooltipTriggerEl) {
            new bootstrap.Tooltip(tooltipTriggerEl);
        });
    
        document.querySelectorAll(".curriculum-icon").forEach(function (element) {
            element.addEventListener("click", function () {
                let pdfUrl = this.getAttribute("data-pdf");
                document.getElementById("pdfViewer").src = pdfUrl;
                let auxModal = new bootstrap.Modal(document.getElementById("auxModal"));
                auxModal.show();
            });
        });
    });
});

// Hide modals code 
// -------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById("auxModal");

    modal.addEventListener("hidden.bs.modal", function () {
        var iframe = modal.querySelector("iframe");
        if (iframe) {
            var src = iframe.src;
            iframe.src = "";
        }
    });
});