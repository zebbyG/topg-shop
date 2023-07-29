const toastTrigger = document.getElementById('liveToastBtn');
const toastLiveExample = document.getElementById('liveToast');
const sessionStorageKey = 'toastShown';

// Function to show the toast
function showToast() {
const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
toastBootstrap.show();
}

// Show the toast on page load regardless of, if "add-to-cart" button is clicked
document.addEventListener('DOMContentLoaded', () => {
const toastShown = sessionStorage.getItem(sessionStorageKey);
if (!toastShown) {
  showToast();
}
});

// Event listener for the add to cart button
toastTrigger.addEventListener('click', () => {
showToast();
});