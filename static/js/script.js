// Display the dropdown menu when clicking the hamburger button
$("#navbar-dropdown-button").on("click", function(event) {
    $(".dropdown").toggleClass("dropdown--visible");
});