document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("uploadForm");
    const statusDiv = document.getElementById("status");
    const loader = document.getElementById("loader");

    form.addEventListener("submit", function() {
        statusDiv.innerHTML = "Converting PDF to Excel... please wait.";
        loader.style.display = "inline-block"; // show spinner
    });

    // When the page reloads after download, reset status
    window.addEventListener("focus", function() {
        if (loader.style.display === "inline-block") {
            loader.style.display = "none";
            statusDiv.innerHTML = "Conversion complete! Your Excel file has been downloaded.";
        }
    });
});
