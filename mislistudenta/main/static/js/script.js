$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});



$(document).ready(function(){

    $('#buy_white').bind('click', function(){
        buy('white')
    });
    $('#buy_red').bind('click', function(){
        buy('red')
        
    });
//    $('#buy_white').hover(function(){
//        width = $('#white_book').width();
//        $('#white_book').width(width*1.1);
//    }, function(){
//        width = $('#white_book').width();
//        $('#white_book').width(width/1.1);
//    });
    $('#order_dialog_btn_step1').live('click', function(){
        validate_form();
    });
    $('#order_dialog_btn_step2').live('click', function(){
        $('#order_dialog button').attr('disabled', 'disabled');
        $('#order_dialog img.hide').removeClass('hide');
        make_order();
    });
    $('#order_dialog_btn_back_step2').live('click', function(){
        get_form();
    });
    $.validationEngine.defaults.autoPositionUpdate = true;

});

function validate_form(){
    validated = $("#order_form").validationEngine('validate');
    if (validated) {
        var form = $("#order_form").serialize();
        $.post("/order/", form,
                function(response){
                    if ( response.success == true ) {
                        $("#order_dialog .content").html(response.html);
                    }
                    else if ( response.success == false ) {
                        alert('false');
                        $("#order_dialog .content").html(response.html);
                    }
                }, "json");
    }
}

function buy(alias){
    get_form(alias);
    $('#order_dialog').modal({
        'backdrop': true,
        'keyboard': true,
        'show': true
    });

    $('#order_dialog').bind('hide', function(){
        $('#order_form').validationEngine('hide');
    })
}

function get_form(alias){
    var form = $("#order_form").serialize();
    if (alias) {
        form = form + "&book=" + alias;
    }
    $.get("/order/", {'form': form},
            function(response){
                $("#order_dialog .content").html(response.html)
                $('#order_form').validationEngine({promptPosition : "centerRight", validationEventTrigger: "submit"});
                $('input').change(function(){
                    $('#order_form').validationEngine('validateField', $(this))
                });
            }, "json")
}

function make_order(){
    var form = $("#order_form").serialize();
    $.post("/order/", form,
            function(response){
                $("#order_dialog .content").html(response.html)
                $('#order_dialog').bind('hide', function(){
                    window.location = ""
                })
            }, "json")
}