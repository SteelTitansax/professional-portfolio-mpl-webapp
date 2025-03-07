document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
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
            let pdfModal = new bootstrap.Modal(document.getElementById("pdfModal"));
            pdfModal.show();
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
            let pdfModal = new bootstrap.Modal(document.getElementById("pdfModal"));
            pdfModal.show();
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
                let pdfModal = new bootstrap.Modal(document.getElementById("pdfModal"));
                pdfModal.show();
            });
        });
    });
});