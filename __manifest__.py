{
    'name': 'Workonweb',
    'version': '1.0',
    'author': 'mubeen',

    'depends':
        [
            'base',
            'web',
            'sale'
        ],

    'data': [
        'views/workonweb_view.xml',
        'views/web_template.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,

}
