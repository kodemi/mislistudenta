$(document).ready(function(){
    $('#order_form').validationEngine();
})

function validate() {
    var form = $("#order_form").serialize();
    $.post("/order/", form,
        function(response){
            if ( response.success == true ) {
                $("#order_form").html(response.html);
            }
            else if ( response.success == false ) {
                $("#order_form").html(response.html);
            }
         }, "json");
};

function validate2(){
    if ( $('#id_lastname').attr('value') == '' ||
        $('#id_firstname').attr('value') == '' ||
        $('#id_email').attr('value') == '' ||
        $('#id_tel').attr('value') == '' ||
        $('#id_quantity').attr('value') == '' ||
        $('#id_payment_method').attr('value') == '' ||
        $('#id_delivery_method').attr('value') == '') {
        $('.empty_field_alert').alert();
    }
    else {
        alert('222')
    }
}