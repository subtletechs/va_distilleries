from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # [VA|IMP|-006] - Vendor must be identified on local and foreign
    vendor_category = fields.Selection([('local', 'Local'), ('foreign', 'Foreign')], string='Vendor Category',
                                       default='local')

