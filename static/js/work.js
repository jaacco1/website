$(function () {
    $('ul#filter a').click(function () {
        $(this).css('outline', 'none');
        $('ul#filter .active').removeClass('active');
        $(this).parent().addClass('active');

        var filterVal = $(this).text().toLowerCase().replace(' ', '-');

        if (filterVal == 'all') {
            $('section#work article.hidden').fadeIn('slow').removeClass('hidden');
        } else {

            $('section#work article').each(function () {
                if (!$(this).hasClass(filterVal)) {
                    $(this).fadeOut('normal').addClass('hidden');
                } else {
                    $(this).fadeIn('slow').removeClass('hidden');
                }
            });
        }

        return false;
    });
});

$(function () {
    $('div#work-list article').hover(function () {
        $('div#work-list article').removeClass('opacity1').addClass('opacity75');
        $(this).removeClass('opacity75').addClass('opacity1');
    }, function () {
        $('div#work-list article').removeClass('opacity75 opacity1');
    });
});