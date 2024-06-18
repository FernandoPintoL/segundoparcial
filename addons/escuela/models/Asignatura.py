from odoo import models, fields

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'escuela.asignatura'

    name = fields.Char(string='Detalle', required=True, unique=True)
    sigla = fields.Char(string='Sigla', required=True, unique=True)
    horario_ids = fields.One2many('escuela.horario', inverse_name='asignatura_id',string='Horario')
    notasasignatura_ids = fields.One2many('escuela.notasasignatura', inverse_name='asignatura_id',string='Notas Asignatura')
    profesor_ids = fields.One2many('escuela.profesor', inverse_name='asignatura_id', string='Profesores')