var sticky = $(".navbar").offset().top;

$(window).scroll(function() {
    if ($(document).scrollTop() > 50) {
        $(".heading-primary").removeClass("heading-primary--sliding-in");
        $(".heading-primary").addClass("heading-primary--sliding-out");
      
        $(".header__logo-box").removeClass("header__logo-box--fadingIn");
        $(".header__logo-box").addClass("header__logo-box--fadingOut");
    }
    else {
        $(".heading-primary").removeClass("heading-primary--sliding-out");
        $(".heading-primary").addClass("heading-primary--sliding-in");
      
        $(".header__logo-box").removeClass("header__logo-box--fadingOut");
        $(".header__logo-box").addClass("header__logo-box--fadingIn");
    }
    
    $("#debug-window").text("scrollTop: " + $(document).scrollTop() + "offset: " + sticky);

    if ($(document).scrollTop() >= sticky) {
        $(".navbar").addClass("navbar--sticky");
    }
    else {
        $(".navbar").removeClass("navbar--sticky");
    }


});