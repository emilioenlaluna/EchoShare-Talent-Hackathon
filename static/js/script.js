document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');

    images.forEach(img => {
        img.style.transition = 'opacity 0.5s';
        img.addEventListener('mouseover', () => {
            img.style.opacity = 0.7;
        });
        img.addEventListener('mouseout', () => {
            img.style.opacity = 1;
        });
    });
});
