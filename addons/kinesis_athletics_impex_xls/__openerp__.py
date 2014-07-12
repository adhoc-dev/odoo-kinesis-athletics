# -*- coding: utf-8 -*-
{
    'active': False,
    'name': 'Import/Export Groups Evaluations',
    'author': 'Ingenieria Adhoc',
    'description': 'Import/Export Groups Evaluations',
    'website': 'www.ingadhoc.com',
    'images': [],
    'category': 'base.module_category_hidden',
    'demo_xml': [],
    'depends': [
        'kinesis_athletics_x', 
    ],
    'description': '',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'test': [],
    'update_xml': [
        'wizard/group_evaluation_export_wizard_view.xml',
        'report/group_evaluation_export_report.xml',
        'group_view.xml',
    ],
    'version':'1.0'
}
