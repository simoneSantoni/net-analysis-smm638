<script>
// Theme-aware logo switcher
document.addEventListener('DOMContentLoaded', function() {
    // Function to update logo based on theme
    function updateLogo() {
        const logo = document.querySelector('.sidebar-logo');
        if (logo) {
            const isDarkMode = document.body.classList.contains('quarto-dark');
            const newSrc = isDarkMode ?
                './imgs/module-icon-dark.svg' :
                './imgs/module-icon-light.svg';

            if (logo.src !== newSrc) {
                logo.src = newSrc;
            }
        }
    }

    // Initial logo update
    updateLogo();

    // Watch for theme changes
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                updateLogo();
            }
        });
    });

    // Start observing the body element for class changes
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['class']
    });

    // Also listen for the Quarto theme toggle
    const themeToggle = document.querySelector('.quarto-color-scheme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            setTimeout(updateLogo, 100); // Small delay to ensure theme has switched
        });
    }
});
</script>
