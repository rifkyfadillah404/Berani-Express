{
    'name': 'Courier Core - Incident Log System',
    'version': '18.0.1.0.0',
    'summary': 'Incident Log System for BeraniExpress',
    'description': """
        A simple Odoo module to manage the lifecycle of internal incidents
        for BeraniExpress logistics provider.
    """,
    'author': 'BeraniExpress',
    'category': 'Operations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/courier_incident_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
