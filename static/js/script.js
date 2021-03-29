// Display the dropdown menu when clicking the hamburger button
$("#navbar-dropdown-button").on("click", function(event) {
    $(".dropdown").toggleClass("dropdown--visible");
    $("#navbar-dropdown-button").toggleClass("navbar__button--active");
});