function performSearch() {
    var selectedColor = document.getElementById("color-filter").value;

    var cards = document.getElementsByClassName("card-text");

    for (var i = 0; i < cards.length; i++) {
        var cardColor = cards[i].dataset.color.toLowerCase();

        if (selectedColor === "all" || cardColor === selectedColor.toLowerCase()) {
            cards[i].style.display = "block";
        } else {
            cards[i].style.display = "none";
        }
    }
}
