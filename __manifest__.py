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
        'data/receipts_data.xml',
        'stock/stock_move.xml',
        'stock/stock_picking_view.xml',
        'base/res_partner_view.xml',
        'purchase/purchase_views.xml',
        'product/product_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': True
}
