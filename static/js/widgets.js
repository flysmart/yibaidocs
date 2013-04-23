var __utils = (function($){

    var highlight_tasks = function(username) {
        if($('#mark_my_tasks:checked').length == 1) {
            _do_highlight_tasks(username, true);
        }

        $('#mark_my_tasks').click(function(){
            _do_highlight_tasks(username, this.checked);

            $.ajax({
                url : g_mark_my_tasks_url + '?mark_my_tasks=' + this.checked,
                type : 'GET',
                //data : {mark_my_tasks : this.checked},
                dataType : 'json',
                success : function(result) {

                },
                error : function(result) {

                }
            });

        });
    };

    var _do_highlight_tasks = function(username, is_checked) {
        $('.schedule_tbl tr').each(function(){
            if(is_checked) {
                var tr_text = $(this).text();
                if(tr_text.indexOf(username) != -1) {
                    $(this).addClass('highlight_task');
                } else {
                    $(this).addClass('fade_task');
                }
            } else {
                $(this).removeClass('highlight_task');
                $(this).removeClass('fade_task');
            }
        });
    }

    var roll_page = function() {
        $('#roll').hide();
        $(window).scroll(function() {
            if($(window).scrollTop() >= 100){
                $('#roll').fadeIn(400);
            } else {
                $('#roll').fadeOut(200);
            }
        });
        $('#roll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});
        $('#roll_bottom').click(function(){$('html,body').animate({scrollTop:$('.footer').offset().top}, 800);});
    };

    return {
        roll_page : roll_page,
        highlight_tasks : highlight_tasks
    };
})(jQuery);

$(document).ready(function(){
    __utils.roll_page();
    var username = $('#sub_title span:eq(1)').text();
    __utils.highlight_tasks(username);
});