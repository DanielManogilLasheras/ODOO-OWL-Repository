from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from collections import defaultdict

class domain_manager(models.Model):
    _name = 'domain.manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'domain_manager'

    name = fields.Char(string="Name", required=True, help="Enter domain name", tracking=True)
    owner = fields.Many2one('res.partner', string="Owner", required=True, copy=False, help="Enter domain owner")
    expire_date = fields.Datetime(default = fields.Datetime.now, help="Enter expiration date", copy=False, tracking=True)
    active_time = fields.Integer(string='Active time', help='Enter the years after which the domain will be renovated automatically', copy=False)
    state = fields.Selection([('draft','Draft'),('active','Active'),('cancelled','Cancelled')], default='draft,', string="Status", readonly=True, required=True, copy=False, index=True, tracking=3)

    def _get_expiring_domains(self):
        date_limit = datetime.now() + timedelta(days = 30)
        expiring_domains = self.env['domain.manager'].search([('state','=','active'),('expire_date','<=',date_limit)])
        domains_by_partner = defaultdict(list)
        for domain in expiring_domains:
            if domain.owner:
                domains_by_partner[domain.owner].append(domain)
        return domains_by_partner

    def _cron_send_expiry_notifications(self):
        domains_by_partner = self._get_expiring_domains()
        template = self.env.ref('domain_manager.mail_template_domain_expiration')
        
        for partner, domains in domains_by_partner.items():
            template.with_context(domains=domains).send_mail(partner.id, force_send=True,raise_exception=True)

    def action_activate(self):
        for record in self:
            if not record.expire_date:
                raise ValidationError('You must stabblish a date before activating a domain')
                return
            if record.state in ('cancelled'):
                raise ValidationError("You can't activate domains in the state: Cancelled, either create a new one or return this Domain to draft state")
                return
            return record.write({'state': 'active'})

    def action_set_draft(self):
        for record in self:
            expire_date = False
            return record.write({'state': 'draft'})
    def action_cancel(self):
        return self.write({'state': 'cancelled'})