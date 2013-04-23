/**
 * User: laonan
 * Date: 13-3-22
 * Time: 11:50 AM
 */

var __feedback = (function($){

    var _hide_editor = function(){
        if (tinyMCE.getInstanceById('id_feedback')) {
            tinyMCE.execCommand('mceFocus', false, 'id_feedback');
            tinyMCE.execCommand('mceRemoveControl', false, 'id_feedback');
            $('.form_feedback').remove();
            $('.submit_feedback').remove();
            $('#feedback_list').remove();
        }

        tinyMCE.triggerSave();

    };

    var _show_editor = function(trigger) {
        $(trigger).after('<div class="form_feedback"><textarea rows="10" cols="40" name="feedback" id="id_feedback"></textarea></div>');
        tinyMCE.init({
            mode : "none",
            theme : "simple",
            width: "600",
            height: "180"
        });
        tinyMCE.execCommand('mceAddControl', false, 'id_feedback');
        tinyMCE.triggerSave();

        var html_feedbacks = '<div class="submit_feedback"><input type="button" class="btn" value="提交" /></div><div id="feedback_list"></div>';
        $('.form_feedback').after(html_feedbacks);

        $.ajax({
            url : g_get_feedback_url + '?workingday_id=' + $(trigger).parent().attr('data-wordingday-id'),
            type : 'get',
            dataType : 'json',
            success : function(result) {
                var tbl = '<table><tbody>';
                var items = eval(result.items);
                for(var i=0; i < items.length; i ++) {
                    tbl += '<tr>';
                    tbl += '<td class="nick_name">' + items[i].fields.nick_name + '</td>';
                    tbl += '<td>' + items[i].fields.feedback + '</td>';
                    tbl += '<td class="datetime">' + items[i].fields.create_datetime + '</td>';
                    tbl += '</tr>';
                }
                tbl += '</tbody></table>';

                $('#feedback_list').html(tbl);
            },
            error : function(result) {

            }
        });

        $('.submit_feedback .btn').click(function(){
            var c = tinyMCE.getInstanceById('id_feedback').getBody().innerHTML;
            $(this).attr('value', '正在提交...');
            $(this).attr('disabled', true);
            $.ajax({
                url : g_submit_feedback_url,
                type : 'post',
                data : {'feedback' : c, 'workingday_id' : $(trigger).parent().attr('data-wordingday-id')},
                dataType : 'json',
                success : function(result) {
                    var nick_name = $('#sub_title span:eq(1)').text();
                    if($('#feedback_list table tr').length > 0) {
                        $('#feedback_list table tr:eq(0)').before('<td class="nick_name">' + nick_name + '</td><td>' + c + '</td><td class="datetime">刚刚</td>');
                    } else {
                        $('#feedback_list').html('<table><tbody><tr><td class="nick_name">' + nick_name + '</td><td>' + c + '</td><td class="datetime">刚刚</td></tr><tbody></table>');
                    }
                },
                error : function(result) {
                    console.log(result);
                },
                complete : function(result){
                    $('.submit_feedback .btn').attr('value', '提交');
                    $('.submit_feedback .btn').attr('disabled', false);
                }
            });
        });
    };

    return {
        hide_editor : _hide_editor,
        show_editor : _show_editor
    };
})(jQuery);

$(document).ready(function(){
    $('.link_feedback').toggle(
        function() {
            __feedback.hide_editor();
            __feedback.show_editor(this);
        },
        function() {
            __feedback.hide_editor();
        }
    );
});
