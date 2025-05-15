# -*- coding: utf-8 -*-
{
    'name': "domain_manager",
    'summary': """
        Domain registry to track expiration dates""",
    'description': """
        This module's purpose is to allow users to create and maintein a record of domains rented by clients, 
        while tracking their expiration dates, activating/deactivating them, and furthermore perform email operations to remind them of near expirations
    """,
    'author': "",
    'website': "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale',],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/domain_manager_views.xml',
        'data/notification_template_data.xml',
        'data/ir_cron_data.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
