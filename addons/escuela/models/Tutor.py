from odoo import models, fields

class Tutor(models.Model):
    _name = 'escuela.tutor'
    _description = 'escuela.tutor'

    name = fields.Char(string='Nombre', required=True)
    apaterno = fields.Char(string='Apellido Paterno', required=True)
    amaterno = fields.Char(string='Apellido Materno', required=True)
    ci = fields.Char(string='Carnet de Identidad', required=True)
    email = fields.Char(string='Email')
    celular = fields.Char(string='Celular')
    alumno_ids = fields.One2many('escuela.alumno', inverse_name='tutor_id', string='Alumno')
    mensualidad_ids = fields.One2many('escuela.mensualidad', inverse_name='tutor_id',string='Mensualidades')