var count = 0;
$(function () {
    $('div#team-bios a').click(function () {
        if (count === 0) {
            $('div.bio').collapse('show');
            count = 1;
            $('div#team-bios a').html('Hide Bio\'s');
        }
        else if (count === 1) {
            $('div.bio').collapse('hide');
            count = 0;
            $('div#team-bios a').html('View Bio\'s');
        }
    });
});