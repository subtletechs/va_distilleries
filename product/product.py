from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class ProductPackaging(models.Model):
    _inherit = "product.packaging"

    # [VA|FUN|-001]- Add Packaging weight
    packaging_weight = fields.Float(string="Packaging weight")
