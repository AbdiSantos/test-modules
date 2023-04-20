# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import email_split

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_cart_products(self):
        order = self.env['sale.order'].sudo().search([('website_id', '=', self.env.context.get('website_id', False)),
                                                       ('state', 'in', ['draft', 'sent'])], limit=1)
        products = []
        for line in order.order_line:
            product = {
                'product_id': line.product_id.id,
                'product_qty': line.product_uom_qty,
                'product_uom': line.product_uom.name,
            }
            products.append(product)
        return products

    def send_quotation_email(self, email_to):
        email_template = self.env.ref('module_name.email_template_quotation')
        mail_values = {
            'subject': 'Nueva cotización de productos',
            'body_html': email_template.body_html,
            'email_from': email_template.email_from,
            'email_to': email_to,
            'res_id': self.id,
            'model': 'sale.order',
        }
        try:
            self.message_post(
                body=email_template.body_html,
                subject='Nueva cotización de productos',
                partner_ids=[],
                email_from=email_template.email_from,
                email_to="abdisantos1004@gmail.com",
                message_type='email',
                subtype='mail.mt_comment',
                **mail_values,
            )
        except Exception as e:
            raise UserError(_("Error al enviar el correo electrónico: %s") % e)
