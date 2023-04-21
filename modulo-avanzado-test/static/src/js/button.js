doo.define('mail_cart.website_cart_test', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');

    $(document).ready(function () {
        // Buscar el botón personalizado y agregarle un evento clic
        $('button#my_cart_button').on('click', function () {
            // Obtener los detalles de los productos en el carrito
            ajax.jsonRpc('/shop/cart/get_order_data', 'call', {
                'compute_tax': false,
                'line_id': false,
            }).then(function (data) {
                // Enviar los detalles de los productos a la consola del navegador
                console.log(data);
            });
        });
    });
});
