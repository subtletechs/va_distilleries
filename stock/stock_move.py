import datetime

from odoo import api, fields, models, _

from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class Picking(models.Model):
    _inherit = "stock.picking"

    # [VA|IMP|-004]- Add new approval level to all operations
    state = fields.Selection(selection_add=[('approved', 'Approved'), ('done',)])

    def action_approve(self):
        self.write({
            'state': 'approved'
        })


class Location(models.Model):
    _inherit = "stock.location"

    # [VA|IMP|-002] - Update Inventory Locations
    mobile_location = fields.Boolean(string="Mobile Location", default=False)
    main_location = fields.Boolean(string="Main Location", default=False)


class Warehouse(models.Model):
    _inherit = "stock.warehouse"

    # [VA|IMP|-002] - Select Warehouse Locations
    warehouses = fields.Selection([('padukka', 'Padukka'), ('boralesgamuwa', 'Boralesgamuwa')], string="Warehouses",
                                  required=True)
