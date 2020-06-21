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
            })
    });

    $('.select').change(function () {
        var t = document.getElementById("teams");
        var tn = t.options[t.selectedIndex].value
        
        $.get(
            '/jobs/', {'team':tn}
        );
        // console.log(tn);
    });    

});