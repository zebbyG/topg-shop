function toggleTheme() {
    const body = document.getElementsByTagName('body')[0];
    body.classList.toggle('light-mode');
    body.classList.toggle('dark-mode');

  // Update the button text based on the current theme
    const themeButton = document.getElementById('theme-toggle-button');
    if (body.classList.contains('dark-mode')) {
    themeButton.textContent = 'Light Mode';
    localStorage.setItem('theme', 'dark');
    } else {
    themeButton.textContent = 'Dark Mode';
    localStorage.setItem('theme', 'light');
    }
}

// Check the theme preference on page load
document.addEventListener('DOMContentLoaded', function () {
    const theme = localStorage.getItem('theme');
    const body = document.getElementsByTagName('body')[0];
    if (theme === 'dark') {
        body.classList.add('dark-mode');
        document.getElementById('theme-toggle-button').textContent = 'Light Mode';
    } else {
        body.classList.add('light-mode');
        document.getElementById('theme-toggle-button').textContent = 'Dark Mode';
    }
});