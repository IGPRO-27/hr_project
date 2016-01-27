# -*- coding: utf-8 -*-
{
    'name': "hr_project_custom",

    'summary': """Link Tasks to projects""",

    'description': """
        Link Tasks to projects:
    """,

    'author': "IGPRO",
    'website': "http://igpro-online.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/templates.xml',
        # 'views/session_workflow.xml',
        # 'views/openacademy.xml',
        # 'views/partner.xml',
        # 'views/session_board.xml',
        'views/hr_project_view.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
