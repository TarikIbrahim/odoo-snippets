# -*- coding: utf-8 -*-
{
    'name': "dynamic-column-label",

    'summary': """
        Making dynamic column label for company_karat_weight column to appear in account_move list view""",

    'description': """
        in account move invoiced list view I want to have one column called company_karat_weight to have dynamic field string value for in list view column name to have this final result 
Weight (K24) while K24 can be anything fetched from the field  company_karat_type
    """,

    'author': "Tarik Ibrahim",
    'website': "https://www.linkedin.com/in/tarikibrahim",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_tree_view.xml',
        'views/company_form_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
