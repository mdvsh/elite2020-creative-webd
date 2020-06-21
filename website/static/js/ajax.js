$(document).ready(function() {
    $('#stat1').click(function() {
    var AppIdVar;
    var UpStatVar;
    AppIdVar = $(this).attr('data-appid');
    UpStatVar = $(this).attr('data-upstat');

    $.get('/staff/update_status/',
        {'app_id': AppIdVar, 'up_stat':UpStatVar},
        function(data) {
            $('#statu').html(data);
            // $('#like_btn').hide();
        })
    });
    $('#stat2').click(function() {
        var AppIdVar;
        var UpStatVar;
        AppIdVar = $(this).attr('data-appid');
        UpStatVar = $(this).attr('data-upstat');
    
        $.get('/staff/update_status/',
            {'app_id': AppIdVar, 'up_stat':UpStatVar},
            function(data) {
                $('#statu').html(data);
                // $('#like_btn').hide();
            })
        });
    $('#stat3').click(function() {
    var AppIdVar;
    var UpStatVar;
    AppIdVar = $(this).attr('data-appid');
    UpStatVar = $(this).attr('data-upstat');

    $.get('/staff/update_status/',
        {'app_id': AppIdVar, 'up_stat':UpStatVar},
        function(data) {
            $('#statu').html(data);
            // $('#like_btn').hide();
        })
    });
});