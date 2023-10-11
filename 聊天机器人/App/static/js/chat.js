function chat(message) {
    $.ajax({
        url: "chat",
        type: "GET",
        data: {
            "message": message
        },
        success: function (data) {
            var ans = '<div class="answer">' +
                '<div class="icon left"><img src="/static/images/ai.png"/></div>' +
                '<div class="answer_text"><p id="content" style="white-space: pre-line;">' + data + '</p><i></i>' +
                '</div><div id="subText"></div><a id="btn" onclick="change()" style="color: blue;"></a></div>';

            $('.speak_box').append(ans);
            fit_screen();
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("服务器出错：" + XMLHttpRequest.status);
        }
    });
}

function key_up() {
    var text = $('.chat_box input').val();
    if (text == '') {
        $('.write_list').remove();
    } else {
        var str = '<div class="write_list">' + text + '</div>';
        $('.footer').append(str);
        $('.write_list').css('bottom', $('.footer').outerHeight());
    }
}

function send_message() {
    $('.write_list').remove();
    var text = $('.chat_box input').val();
    // var text = $('.chat_box input').val();
    if (text == '') {
        alert('请输入聊天内容！');
        $('.chat_box input').focus();
        //      $('body').css('background-image', 'url(/images/bg.jpg)');
        $('body').css('background-image', 'url_for(/static/images/bg.jpg)');

    } else {
        var str = '<div class="question">' +
            '<div class="icon right"><img src="/static/images/me.png"/></div>' +
            '<div class="question_text clear">'+ text +
            '</div></div>';

        $('.speak_box').append(str);
        $('.chat_box input').val('');
        $('.chat_box input').focus();

        fit_screen();
        auto_width();
        chat(text);
    }
}
function fit_screen() {
    $('.speak_box, .speak_window').animate({
        scrollTop: $('.speak_box').height()
    }, 500);
}

function auto_width() {
    $('.question_text').css('max-width', $('.question').width() - 60);
}

function getcjwt(message) {
    var text = String(message);
//   alert(text);
    var str = '<div class="question">' +
        '<div class="icon right"><img src="/static/images/me.png"/></div>' +
        '<div class="question_text clear">' + text + '<i></i>' +
        '</div></div>';

    $('.speak_box').append(str);
    $('.chat_box input').val('');
    $('.chat_box input').focus();

    fit_screen();
    auto_width();
    chat(text);
}
