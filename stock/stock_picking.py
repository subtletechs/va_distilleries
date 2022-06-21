from odoo import SUPERUSER_ID, _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # [VA|IMP|-004]- Add new approval level to all operations
    state = fields.Selection(selection_add=[('approved', 'Approved'), ('done',)])

    def action_approve(self):
        self.write({
            'state': 'approved'
        })

    def button_validate(self):
        """In here We will check negative quantities and block it for specific inventory operations"""
        # 1. Delivery Orders
        if self.picking_type_code == 'outgoing':
            stock_moves = self.move_ids_without_package
            for stock_move in stock_moves:
                product_id = stock_move.product_id
                done_qty = stock_move.quantity_done
                # check tracking method
                tracking_method = product_id.tracking
                if tracking_method in ['lot', 'serial']:
                    move_lines = stock_move.move_line_ids
                    for move_line in move_lines:
                        lot = move_line.lot_id
                        qty_done = move_line.qty_done
                        if qty_done > lot.product_qty:
                            error = "Lot "+lot.name+" Don't have enough quantities"
                            raise ValidationError(error)
                elif tracking_method == 'none':
                    if done_qty > product_id.qty_available:
                        error = product_id.name+ "Doesn't have enough quantity"
                        raise ValidationError(error)
        return super(StockPicking, self).button_validate()