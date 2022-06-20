{
    'name': 'VA Distilleries',
    'version': '1',
    'website': 'https://www.subtletechs.com/',
    'author': 'Subtle Technologies (Pvt) Ltd',
    'depends': [
        'base',
        'stock',
        'purchase',
    ],
    'data': [
        'data/warehouses.xml',
        'data/locations.xml',
        'stock/stock_move.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': True
}
