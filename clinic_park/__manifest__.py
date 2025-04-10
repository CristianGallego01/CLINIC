{
    'name': 'clinic_park',
    'version': '1.0.1',
    'depends': ['base', 'account'],
    'data': [
        'views/clinic_park_views.xml',       # Carga primero vistas/modelos
        'views/clinic_park_menus.xml',
        'security/ir.model.access.csv',      # Luego permisos
    ],
    'application': True,
    'installable': True,
}