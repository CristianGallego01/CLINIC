{
    'name': 'clinic_park',
    'version': '1.0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',  # Carga primero los permisos de acceso
        'views/clinic_park_patient_view.xml',
        'views/clinic_park_triage_view.xml',
        'views/clinic_park_menus.xml',

    ],
    'application': True,
    'installable': True,
}