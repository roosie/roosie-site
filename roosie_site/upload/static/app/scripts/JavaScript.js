$(window).resize(function () {
    var viewportW = $(window).width();
    if (viewportW < 768) {
        $('#wrapper').removeClass('toggled')
    }
});