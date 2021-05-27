// Display the dropdown menu when clicking the hamburger button
$("#navbar-dropdown-button").on("click", function(event) {
    $(".dropdown").toggleClass("dropdown--visible");
});

$(".comment--clickable").on("click", function(event) {
    //alert("Comment clicked");
});

// Switch to dark mode when the checkbox is clicked
$("#dark-mode-switch").change(function() {
    if(this.checked) {
        $(":root").css("--color-neutral-900", "white");
        $(":root").css("--color-neutral-000", "black");
    }
    else {
        $(":root").css("--color-neutral-900", "black");
        $(":root").css("--color-neutral-000", "white");
    }
});