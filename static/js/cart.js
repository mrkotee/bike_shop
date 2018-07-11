//var cart = {
//    add: function (pk, quantity) {
//      quantity = quantity || 1
//      return $.post(URLS.addItem, {pk: pk, quantity: quantity}, 'json')
//    }
//
//    remove: function (pk) {
//      return $.post(URLS.removeItem, {pk: itemPK}, 'json')
//    }
//
//    changeQuantity: function (pk, quantity) {
//      return $.post(URLS.changeQuantity, {pk: pk, quantity: quantity}, 'json')
//    }
//
//    empty: function () {
//      $.post(URLS.emptyCart, 'json')
//    }
//}

var frm = $('.btn_form');
frm.submit(function () {
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
//        success: function (data) {
//            alert(data);
//        },
//        error: function(data) {
//            alert("Something went wrong!");
//        }
    });
    return false;
});


$(".quantity").change(function () {
    var form = $(this).closest("form");
    $.ajax({
        type: form.attr('method'),
        url: form.attr("action"),
        data: form.serialize(),
        success: function (data) {
          if (data.is_taken) {
            alert(data.error_message);
          }
        }
        });
    return false;
    });

$('.close1').on('click', function(){
    var form = $(this).closest("form");
    $.ajax({
        type: form.attr('method'),
        url: form.attr("action"),
        data: form.serialize(),
        success: function (data) {
            form.parent().fadeOut('slow', function(){
            form.parent().remove();
            location.reload();
            });
        }
    });

    return false;
    });





