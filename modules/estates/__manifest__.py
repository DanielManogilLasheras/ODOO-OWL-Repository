{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Daniel",
    'summary' : 'Find the best Real Estate offers',
    'category': 'Sales',
    'description': """
    Description text
    """,
    'depends':['base'],
    'application': 'True',

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml'
    ]
}

