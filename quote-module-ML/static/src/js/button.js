odoo.define('my_custom_module.send_quotation', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');

    publicWidget.registry.SendQuotationButton = publicWidget.Widget.extend({
        selector: '.send_quotation_button',
        events: {
            'click': '_onClick',
        },
        _onClick: function () {
            var email_to = this.$el.closest('.js_cart').find('input[name="email_quotation"]').val();
            var self = this;
            self.$el.prop('disabled', true);
            this._rpc({
                route: '/shop/send_quotation',
                params: {
                    email_to: email_to,
                },
            }).then(function () {
                self.$el.prop('disabled', false);
                self.$el.after('<span class="sent_message">Se ha enviado la cotización a su correo electrónico</span>');
                self.$el.hide();
            });
        }
    });
});
