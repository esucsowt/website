// BACK TO TOP BUTTON
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 100) {
        $('.back-to-top').fadeIn();
    } else {
        $('.back-to-top').fadeOut();
    }
});
$(document).ready(function() {
    $(".back-to-top").click(function(event) {
        event.preventDefault();

        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

});

window.onload = function()
{
  $('.owl-carousel').owlCarousel({
    items: 8,
    loop:true,
    autoplay:true,
    margin:10,
    nav:true,
    autoplayTimeout:1000,
    autoplayHoverPause:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})
}