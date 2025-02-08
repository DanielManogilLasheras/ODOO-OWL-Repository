# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

class Student(models.Model):
    _name = "school.student"
    _description = "Tabla de Estudiantes"
    
    name = fields.Char(string="Nombre", required = True)
    age = fields.Integer(string="Edad")

# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

