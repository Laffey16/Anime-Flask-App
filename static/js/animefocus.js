document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("image-modal");
    const modalImg = document.getElementById("modal-image");
    const images = document.querySelectorAll(".grid-image");
    const span = document.getElementsByClassName("close")[0];
    const loader = document.getElementById("loader");

    // Function to open modal
    function openModal(imageSrc) {
        console.log("Opening modal with image:", imageSrc);
        modal.style.display = "flex";
        loader.style.display = "block";
        modalImg.style.display = "none";

        modalImg.onload = function () {
            loader.style.display = "none";
            modalImg.style.display = "block";
        };

        modalImg.src = imageSrc;
        document.body.style.overflow = 'hidden';
    }

    // Function to close modal
    function closeModal() {
        console.log("Closing modal");
        modal.style.display = "none";
        document.body.style.overflow = 'auto';
    }

    // Event listener for images
    images.forEach((image, index) => {
        image.onclick = function () {
            console.log(`Image ${index} clicked:`, this.src);
            openModal(this.src);
        };
    });

    // Event listener for close button
    if (span) {
        span.onclick = closeModal;
    } else {
        console.error("Close button not found");
    }

    // Event listener for clicking outside the image
    window.onclick = function (event) {
        if (event.target === modal) {
            closeModal();
        }
    };

    // Event listener for Escape key
    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    console.log("Event listeners attached");
});