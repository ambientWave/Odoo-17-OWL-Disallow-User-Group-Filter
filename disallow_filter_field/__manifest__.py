# -*- coding: utf-8 -*-
{
    'name': "Disallow users to use a certain field in filter",

    'summary': "Disallow users to use a certain field in filter in a certain model",

    'description': """
    """,

    'author': "Mina Samir Wahib",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'purchase'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {'web.assets_backend': [
        'disallow_filter_field/static/src/js/DisallowFilterForField.js'
    ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

