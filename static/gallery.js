document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.gallery');
    const images = document.querySelectorAll('.gallery img');
    const imageWidth = images[0]?.clientWidth || 0; // Get the width of a single image
    const totalImages = images.length;

    if (!gallery) {
        console.error('Gallery element not found.');
        return;
    }

    let currentIndex = 0;

    function updateGallery() {
        const offset = -currentIndex * (imageWidth + 10); // Include gap in the offset calculation
        gallery.style.transform = `translateX(${offset}px)`;
    }

    // Swipe functionality
    let startX = 0;

    gallery.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
    });

    gallery.addEventListener('touchend', (e) => {
        const endX = e.changedTouches[0].clientX;

        if (startX - endX > 50 && currentIndex < totalImages - 1) {
            // Swipe left
            currentIndex++;
        } else if (endX - startX > 50 && currentIndex > 0) {
            // Swipe right
            currentIndex--;
        }

        updateGallery();
    });
});
