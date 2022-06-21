from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # [VA|IMP|-007]- New approval level add to the RfQ
    state = fields.Selection(selection_add=[('initial_approve', 'Initial Approve'), ('to approve',)])

    # [VA|IMP|-007]- New approval level add to the RfQ
    def action_approve(self):
        self.write({
            'state': 'initial_approve'
        })

    def button_confirm(self):
        for order in self:
            if order.state not in ['initial_approve', 'sent']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order._approval_allowed():
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
            if order.partner_id not in order.message_partner_ids:
                order.message_subscribe([order.partner_id.id])
        return True
