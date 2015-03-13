{
    'name' : 'Last viewed records',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev, Odoo Community Association (OCA)',
    'category' : 'Base',
    'website' : 'https://yelizariev.github.io',
    'depends' : ['web', 'mail'],
    'data':[
        'views.xml',
        ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
    'installable': True
}
