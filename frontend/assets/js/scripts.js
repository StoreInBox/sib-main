(function($) {

    // scroll by click discover more
    function scrollToContent() {
        var trigger = $('[data-front="scroll-to-content"]');
        var windowHeight = $(window).height();
        trigger.click(function() {
            $('html, body').animate({
              scrollTop: windowHeight
            }, 1000);
        });
    }

    // equal height
    function equalheight(container) {

        var currentTallest = 0,
        currentRowStart = 0,
        rowDivs = new Array(),
        $el,
        topPosition = 0;

        $(container).each(function() {

            $el = $(this);
            $($el).height('auto')
            topPostion = $el.position().top;

            if (currentRowStart != topPostion) {
                for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
                    rowDivs[currentDiv].height(currentTallest);
                }
                rowDivs.length = 0; // empty the array
                currentRowStart = topPostion;
                currentTallest = $el.height();
                rowDivs.push($el);
            } else {
                rowDivs.push($el);
                currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
            }
            for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
                    rowDivs[currentDiv].height(currentTallest);
            }
        });
    }

    // document ready
    $(window).on('load', function() {
        scrollToContent();
        equalheight('[data-front="product-list"] [data-front="product-list-item"]');
    });

    // all initial on window resize
    $(window).on('resize', function() {
        equalheight('[data-front="product-list"] [data-front="product-list-item"]');
    });


})(jQuery);
