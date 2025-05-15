from odoo import models, fields, api, _
import logging
import re
from odoo.exceptions import ValidationError
from datetime import date, timedelta
_logger = logging.getLogger(__name__)
class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.model
    def action_confirm(self):
        domain_regex = re.compile(r'\b[\w-]+\.[\w-]+\b')
        for order in self:
            if not any(domain_regex.search(line.name or '') for line in order.order_line):
                raise ValidationError("You must enter the domain name in the description in order to validate the quotation.")
        
        res = super().action_confirm()
        for order in self:
            domain_lines = order.order_line.filtered(lambda ln: 'Domain' in ln.product_id.name)
            for line in domain_lines:
                qty = int(line.product_uom_qty)
                for i in range(qty):
                    base_name = line.name.strip()
                    suffix = f"-{i+1}" if qty > 1 else ""
                    domain = self.env['domain.manager'].create({
                        'name': f"{base_name}{suffix}",
                        'owner': order.partner_id.id,
                        'state': 'draft',
                    })
                    _logger.info('CREATED SUCCESSFULLY')
                    #Create activity.
                    model_domain = self.env['ir.model'].search([('model', '=', 'domain.manager')], limit=1)
                    self.env['mail.activity'].create({
                        'res_model_id': model_domain.id,
                        'res_model': 'domain.manager',
                        'res_id': domain.id,
                        'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                        'summary': _('Set expiration date'),
                        'note': _('This domain is in draft. Please set an expiration date and confirm it'),
                        'user_id': self.env.user.id,
                        'date_deadline': date.today() + timedelta(days=3),
                    })
        return res
