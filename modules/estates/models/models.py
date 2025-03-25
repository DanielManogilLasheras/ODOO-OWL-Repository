from odoo import models,fields, api
from odoo.exceptions import ValidationError
import datetime
class Property(models.Model):
    _name = "estates.property"
    _description = "Estates model"
    
    name = fields.Char(string='Name', required=True, default= "Unknown")
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    description= fields.Text (string='Description')
    postcode = fields.Char (string = 'Postcode')
    date_availability = fields.Date (string = 'Available from', copy="False", default=datetime.datetime.now() + datetime.timedelta(days=90))
    expected_price = fields.Float (string = 'Expected price', required=True)
    selling_price = fields.Float (string ='Selling price', readonly=True, copy="False")
    bedrooms = fields.Integer (string = 'Bedrooms' , default="2")
    living_area = fields.Integer (string = 'Living area (sqm)')
    facades = fields.Integer (string = 'Facades')
    garage = fields.Boolean (string = 'Garage')
    garden = fields.Boolean (string = 'Garden')
    garden_area = fields.Integer (string = 'Garden Area (sqm)')
    garden_orientation = fields.Selection(string = 'Garden orientation', selection=[('north','North'),('south','South'),('east','East'),('west','West')])
    active = fields.Boolean(string = "Active", default = "False")
    state = fields.Selection(string = "State" , selection=[("new","New"),("offerReceived","Offer Received"),("offerAccepted","Offer Accepter"),("sold","Sold"),("cancelled","Cancelled")], copy="False", readonly = True, default="new")
    property_type_id = fields.Many2one ('estates.property.type', string = "Property Type")
    salesman = fields.Many2one ("res.users", copy="False", string= "Salesman", default=lambda self: self.env.user)
    buyer =  fields.Many2one ("res.partner", string = "Buyer")
    tag_ids = fields.Many2many("estates.property.tag")
    offer_ids = fields.One2many("estates.property.offer", "property_id")
    total_area = fields.Float(compute = "_compute_totalArea", string="Total area (sqm):")
    best_offer = fields.Float(compute = "_compute_bestOffer", string = "Best offer: ")
    
    @api.depends("living_area","garden_area")
    def _compute_totalArea(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    @api.depends ("offer_ids")
    def _compute_bestOffer(self):
        total = 0
        for item in self.offer_ids:
            if self.best_offer < item.price:
                total = item.price
        self.best_offer = total
    @api.onchange("garden")
    def _onchange_hasGarden(self):
        if self.garden:
            if self.garden_area < 10:
                self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ""
    def action_sold(self):
        for record in self:
            if record.state == "cancelled":
                raise ValidationError ("A cancelled property can't be sold")
            else:
                record.state = "sold"
    def action_cancel(self):
        for record in self:
            if record.state == "sold":
                raise ValidationError ("A sold property can't be cancelled")
            else:
                record.state = "cancelled"
    def action_clear_offer(self):
        for record in self:
            if record.state != "cancelled" or record.state  != "sold":
                for element in record.offer_ids:
                    if element.partner_id == record.buyer:
                        element.status = "refused"
                        record.buyer = ""
                        record.selling_price = ""
            else:
                raise ValidationError ("You can't clear the offer of a sold or cancelled property")
class Offer(models.Model):
    _name="estates.property.offer"
    _description="property offer model"
    price = fields.Float(string = "Price")
    partner_id = fields.Many2one ("res.partner", string="Partner", required =  True)
    status = fields.Selection(string = "Status", copy = False, selection=[("accepted","Accepted"),("refused","Refused")])
    validity = fields.Integer (string = "Validity (days):", default = 7, store = True)
    deadline = fields.Datetime(compute="_compute_deadline", inverse="_inverse_deadline", string = "Deadline:", store =  True)
    property_id = fields.Many2one("estates.property", string = 'Property',required = True, )
    @api.depends ("validity")
    def _compute_deadline(self):
        for record in self:
            result = datetime.datetime.now() + datetime.timedelta(days=record.validity)
            record.deadline = result
    def _inverse_deadline(self):
        for record in self:
            delta= record.deadline - datetime.datetime.now() 
            record.validity = delta.days
    def action_accept_offer(self):
        for record in self:
            if  not record.property_id.buyer:
                record.status = "accepted"
                record.property_id.buyer = record.partner_id
                record.property_id.selling_price = record.price
            else:
                raise ValidationError ("The property has been sold to another buyer")
    def action_decline_offer(self):
        for record in self:
            if record.status == "refused":
                raise ValidationError ("This offer has been already refused")
            else:
                record.status = "refused"
class Type(models.Model):
    _name="estates.property.type"
    _description="property type model"
    name = fields.Char (string = "name", required = True)

class Tag(models.Model):
    _name="estates.property.tag"
    _description = "property tag model"
    name = fields.Char (string = "name")

    