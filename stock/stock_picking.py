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
        # Delivery orders/  Internal Transfers
        if self.picking_type_code in ['outgoing', 'internal']:
            stock_moves = self.move_ids_without_package
            for stock_move in stock_moves:
                product_id = stock_move.product_id
                done_qty = stock_move.quantity_done
                # check tracking method
                tracking_method = product_id.tracking
                if tracking_method in ['lot', 'serial']:
                    if stock_move.move_line_ids:
                        move_lines = stock_move.move_line_ids
                        for move_line in move_lines:
                            location_id = move_line.location_id
                            lot = move_line.lot_id
                            qty_done = move_line.qty_done
                            # check the availability of quantity
                            stock_quant = self.env['stock.quant'].search(
                                [('location_id', '=', location_id.id),
                                 ('product_id', '=', product_id.id),
                                 ('lot_id', '=', lot.id)])
                            if stock_quant:
                                quantity = stock_quant.quantity
                                if quantity < qty_done:
                                    error = "Product " + str(product_id.name) + ", Lot " + str(
                                        lot.name) + " Dose not have enough quantities at " + str(location_id.name)
                                    raise ValidationError(error)
                            else:
                                error = "Product " + str(product_id.name) + ", Lot " + str(
                                    lot.name) + " Dose not have enough quantities at " + str(location_id.name)
                                raise ValidationError(error)

                elif tracking_method == 'none':
                    if stock_move.move_line_ids:
                        move_lines = stock_move.move_line_ids
                        for move_line in move_lines:
                            location_id = move_line.location_id
                            qty_done = move_line.qty_done
                            stock_quant = self.env['stock.quant'].search(
                                [('location_id', '=', location_id.id),
                                 ('product_id', '=', product_id.id)])
                            if stock_quant:
                                quantity = stock_quant.quantity
                                if quantity < qty_done:
                                    error = "Product " + str(
                                        product_id.name) + " Dose not have enough quantities at " + str(
                                        location_id.name)
                                    raise ValidationError(error)
                            else:
                                error = "Product " + str(
                                    product_id.name) + " Dose not have enough quantities at " + str(location_id.name)
                                raise ValidationError(error)
        return super(StockPicking, self).button_validate()
