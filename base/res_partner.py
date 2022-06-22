from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # [VA|IMP|-006] - Vendor must be identified on local and foreign
    vendor_category = fields.Selection([('local', 'Local'), ('foreign', 'Foreign')], string='Category',
                                       default='local')

    # VA|IMP|-008 Is Customer ? Is Vendor ? Separation
    # is_customer = fields.Boolean(string="Is Customer", default=False)
    # customer_id = fields.Char(string="Customer ID")
    # is_supplier = fields.Boolean(string="Is Supplier", default=False)
    # supplier_id = fields.Char(string="Supplier ID")

