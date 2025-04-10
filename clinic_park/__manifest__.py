{
    'name': 'clinic_park',
    'version': '1.0.1',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',  # Carga primero los permisos de acceso
        'views/clinic_park_views.xml',       # Carga primero vistas/modelos
        'views/clinic_park_menus.xml',

    ],
    'application': True,
    'installable': True,
}