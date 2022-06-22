from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # [VA|IMP|-007]- New approval level add to the RfQ
    state = fields.Selection(selection_add=[('initial_approve', 'Initial Approve'), ('sent',)])

    # [VA|IMP|-007]- New approval level add to the RfQ
    def action_approve(self):
        self.write({
            'state': 'initial_approve'
        })

    def button_confirm(self):
        for order in self:
            # draft replace to initial_approve
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

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        if self.env.context.get('mark_rfq_as_sent'):
            # Set status to sent after sent email
            self.filtered(lambda o: o.state == 'initial_approve').write({'state': 'sent'})
        return super(PurchaseOrder, self.with_context(
            mail_post_autofollow=self.env.context.get('mail_post_autofollow', True))).message_post(**kwargs)

