# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteSale(http.Controller):
    @http.route(['/shop/cart/update_quote'], type='http', auth="public", website=True, sitemap=False)
    def action_add_to_quote(self, **post):
        order = request.website.sale_get_order()
        products = order.get_cart_products()
        # Aquí puedes enviar los productos por correo electrónico para crear una cotización
        
        # Redireccionamos a la página de carrito
        return request.redirect('/shop/cart')
