    var cards = document.getElementsByClassName("card");

    function performSearch() {
        var searchQuery = document.getElementById("search-input").value.toLowerCase();

        for (var i = 0; i < cards.length; i++) {
            var cardTitle = cards[i].getElementsByClassName("card-title")[0].innerText.toLowerCase();
            var cardText = cards[i].getElementsByClassName("card-text")[0].innerText.toLowerCase();

            if (cardTitle.includes(searchQuery) || cardText.includes(searchQuery)) {
                cards[i].style.display = "block";
            } else {
                cards[i].style.display = "none";
            }
        }

        document.getElementById("search-input").value = searchQuery;
        document.getElementById("search-button").innerText = "Search: " + searchQuery;
        return True; // Prevent form submission
    }