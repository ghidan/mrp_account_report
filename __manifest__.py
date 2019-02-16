# -*- coding: utf-8 -*-
{
    'name': "MRP Account Report",
    'summary': """MRP Account Report""",
    'description': """ Consumption Reporting and Manufacturing Cost Model""",
    'website': "",
    'category': 'Manufacturing',
    'version': '0.1',
    'license': 'AGPL-3',
    'depends': ['base', 'mrp', 'account', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_costing.xml',
        'wizard/consumption_report.xml',
        'views/report_consumption.xml',
        'views/summary_consumption_report.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
