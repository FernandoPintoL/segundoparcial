# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class escuela(models.Model):
#     _name = 'escuela.escuela'
#     _description = 'escuela.escuela'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Profesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'escuela.profesor'

    name = fields.Char(string='Nombre', required=True)
    ci = fields.Char(string='CI', required=True, unique=True)
    email = fields.Char(string='Email', required=True)
    celular = fields.Char(string='Celular')
    horario_ids = fields.One2many('escuela.horario', inverse_name='profesor_id',string='Horario')
    asignatura_id = fields.Many2one('escuela.asignatura', inverse_name='profesor_ids',string='Asignatura')