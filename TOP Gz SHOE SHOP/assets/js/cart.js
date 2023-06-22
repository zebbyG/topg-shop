var updateBtns = document.getElementsByClassName('update-cart');

function handleAddToCart(event) {
  event.preventDefault();

  // Check if the user is authenticated
  if (!user) {
    // Redirect the user to the login page
    var nextUrl = encodeURIComponent(window.location.href);
    window.location.href = "{% url 'accounts:log_in' %}?next=" + nextUrl;
    return;
  }

  // Proceed with adding the item to the cart
  var productId = this.dataset.product;
  var action = this.dataset.action;
  console.log('productId:', productId, 'action:', action);
  console.log('USER:', user);

  // Add your logic to update the cart here
  // ...
}

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', handleAddToCart);
}
