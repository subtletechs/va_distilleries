import datetime

from odoo import api, fields, models, _

from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class Warehouse(models.Model):
    _inherit = "stock.warehouse"

    # [VA|IMP|-002] - Select Warehouse Locations
    warehouses = fields.Selection([('padukka', 'Padukka'), ('boralesgamuwa', 'Boralesgamuwa')], string="Warehouses",
                                  required=True)
