# -*- coding: utf-8 -*-
{
    'name': 'Agregar a Cotización',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Reemplaza el botón de compra para agregar productos a una cotización en el website',
    'description': """Este módulo personalizado para Odoo 16 reemplaza el botón de compra por un botón que agrega los productos a una cotización en el website.""",
    'author': 'Abdi Santos',
    'depends': ['website_sale'],
    'data': [
        'views/website_sale_cart.xml',
        'static/src/js/button.js'
    ],
     'qweb': [
        'static/src/xml/send_quotation_button.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
