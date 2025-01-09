document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.gallery');
    const images = document.querySelectorAll('.gallery img');
    const totalImages = images.length;
    let currentIndex = 0;

    function updateGallery() {
        images.forEach((image, index) => {
            if (index === currentIndex) {
                image.classList.add('active'); // Add active class to the current image
            } else {
                image.classList.remove('active'); // Remove active class from all images
            }
        });    
    }

    // Handle click on the Previous button
    const prevButton = document.querySelector('.prev-btn');
    const nextButton = document.querySelector('.next-btn');

    prevButton.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--; // Move to the previous image
        } else {
            currentIndex = totalImages - 1; // Loop back to the last image if at the start
        }
        updateGallery();
    });

    nextButton.addEventListener('click', () => {
        if (currentIndex < totalImages - 1) {
            currentIndex++; // Move to the next image
        } else {
            currentIndex = 0; // Loop back to the first image if at the end
        }
        updateGallery();
    });
    
    updateGallery(); // Initial gallery setup to show the first image
});
