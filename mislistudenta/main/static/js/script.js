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



jQuery(function() {
	jQuery.support.placeholder = false;
	test = document.createElement('input');
	if('placeholder' in test) jQuery.support.placeholder = true;
});


$(document).ready(function(){

    $("#id_delivery_method").live('change', function(){
        if ( $(this).attr('value') == 'pickup' ){
            $("#id_city").parent().parent().hide();
            $("#id_address").parent().parent().hide();
             $("#id_city").validationEngine('hide');
            $("#id_address").validationEngine('hide');
            deliv_info = $("#delivery_info");
            if (deliv_info) {
                 deliv_info.remove();
            }
        } else if ( $(this).attr('value') == 'courier' ) {
            $("#id_city").parent().parent().show();
            $("#id_address").parent().parent().show();
            $(this).parent().after(window.delivery_info);
            $("#id_city").attr('value', 'Москва').addClass('disabled').attr('disabled', '')
        } else {
            $("#id_city").parent().parent().show();
            $("#id_address").parent().parent().show();
//            $(this).parent().append(delivery_info);
            $("#id_city").attr('value', '').removeClass('disabled').removeAttr('disabled')
        }
    });

    $(".book_link").fancybox({
		'hideOnContentClick': true
	});

    $('#buy_white').bind('click', function(){
        buy('white')
    });

    $('#buy_red').bind('click', function(){
        buy('red')
    });

    $('#buy_blond').bind('click', function(){
        buy('blond')
    });

    $('#buy_white').hover(function(){
        enlarge_book($("#white_book img"), 6)
    }, function(){
        enlarge_book($("#white_book img"), -6)
    });

    $('#buy_red').hover(function(){
        enlarge_book($("#red_book img"), 6)
    }, function(){
        enlarge_book($("#red_book img"), -6)
    });

    $('#buy_blond').hover(function(){
        enlarge_book($("#blond_book img"), 6)
    }, function(){
        enlarge_book($("#blond_book img"), -6)
    });

    $('#order_dialog_btn_step1').live('click', function(){
        validate_form();
    });

    $('#order_dialog_btn_step2').live('click', function(){
        $(this).removeClass('btn').addClass('hide');
        $('#order_dialog_btn_back_step2').attr('disabled', 'disabled');
        $('#loader').removeClass('hide');
        make_order();
    });
    $('#order_dialog_btn_back_step2').live('click', function(){
        get_form();
    });
    $.validationEngine.defaults.autoPositionUpdate = true;

    $('#subscribe').live('change', function(){
        order_number = $('#order_number').text();
        $.post("/subscribe/" + order_number, {'subscribed': $(this)[0].checked}, function(){}, "json")
    })

});

function validate_form(){
    validated = $("#order_form").validationEngine('validate');
    if (validated) {
        if ( $("#id_delivery_method").attr('value') == 'pickup' ){
            $('#id_city').attr('value', '');

            $('#id_address').attr('value', '');
        } else {
            $('#id_city').removeAttr('disabled')
        }
        var form = $("#order_form").serialize();
        $.post("/order/", form,
                function(response){
                    $("#order_dialog .content").html(response.html)
                }, "json");
    }
}

function buy(alias){
    get_form(alias);
    $('#order_dialog').modal({
        'backdrop': "static",
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
                $("#order_dialog .content").html(response.html);
                window.delivery_info = "<div id='delivery_info' ><p class='span4'>Стоимость доставки: " + $("#delivery_price").attr("data-delivery_price") + " руб.</p></div>"
                $("#id_delivery_method").change();
                $('#order_form').validationEngine({promptPosition : "centerRight", validationEventTrigger: "submit"});
                $('input').change(function(){
                    $('#order_form').validationEngine('validateField', $(this))
                });
            }, "json");
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

function enlarge_book(book, inc){
    width = book.width();
    height = book.height();
    offset = book.offset();
    book.width(width + inc);
    book.height(height + inc);
    book.offset({ left: offset.left - inc/2, top: offset.top });
}

function placeholder(){
	if(!$.support.placeholder) {
		var active = document.activeElement;
		$(':text').focus(function () {
			if ($(this).attr('placeholder') != '' && $(this).val() == $(this).attr('placeholder')) {
				$(this).val('').removeClass('hasPlaceholder');
			}
		}).blur(function () {
			if ($(this).attr('placeholder') != '' && ($(this).val() == '' || $(this).val() == $(this).attr('placeholder'))) {
				$(this).val($(this).attr('placeholder')).addClass('hasPlaceholder');
			}
		});
		$(':text').blur();
		$(active).focus();
		$('form').submit(function () {
			$(this).find('.hasPlaceholder').each(function() { $(this).val(''); });
		});
	}
};

