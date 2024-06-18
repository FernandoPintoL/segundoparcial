from odoo import models, fields

class Alumno(models.Model):
    _name = 'escuela.alumno'
    _description = 'escuela.alumno'

    name = fields.Char(string='Nombre', required=True)
    apaterno = fields.Char(string='Apellido Paterno', required=True)
    amaterno = fields.Char(string='Apellido Materno', required=True)
    rude = fields.Char(string='RUDE', required=True, unique=True)
    ci = fields.Char(string='CI', required=True, unique=True)
    fechanacimiento = fields.Date(string='Fecha de nacimiento')
    email = fields.Char(string='Email')
    celular = fields.Char(string='Celular')
    tutor_id = fields.Many2one('escuela.tutor', inverse_name='alumno_ids', string='Tutor')
    inscripcion_ids = fields.One2many('escuela.inscripcion', inverse_name='alumno_id',string='Inscripcion')
    horario_ids = fields.One2many('escuela.horario', inverse_name='alumno_id',string='Horario')
    notasasignatura_ids = fields.One2many('escuela.notasasignatura', inverse_name='alumno_id',string='Notas Asignatura')