$(document).ready(function() {
// Add a click event listener to the delete icon
$('#delete-profile-picture').click(function(e) {
  e.preventDefault(); // Prevent the default link behavior

  // Perform an AJAX request to delete the profile picture
  $.ajax({
    url: '{% url 'accounts:delete_profile_picture' %}',
    method: 'POST',
    data: {
      'user_id': '{{ user.id }}',
      'csrfmiddlewaretoken': '{{ csrf_token }}' // Include the CSRF token
    },
    success: function(response) {
      // Replace the profile picture with the default image
      $('#profile-image').attr('src', '{% static 'default-profile-pic.png' %}');
    },
    error: function(xhr, status, error) {
      // Handle the error if the deletion fails
      console.log(error);
    }
  });
});
});