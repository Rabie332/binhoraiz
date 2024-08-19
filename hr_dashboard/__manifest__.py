{
    "name": "HR Dashboard",
    "version": "17.0.1.0.0",
    "depends": [
        "dashboard_base",
        "hr_base",
    ],
    "author": "Hadooc",
    "data": [
        # "views/assets.xml",
        "views/dashboard_menuitem_views.xml",
    ],
    # "qweb": ["static/src/xml/dashboard_templates.xml"],
    
    "assets": {
        'web.assets_backend': [
            'hr_dashboard/static/src/js/hr_dashboard.js',
            'hr_dashboard/static/src/xml/dashboard_templates.xml'
        ],

},
    
    
    "installable": True,
    "license": "AGPL-3",
}
