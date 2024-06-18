from odoo import fields, models

class Inscripcion(models.Model):
    _name = 'escuela.inscripcion'
    _description = 'escuela.inscripcion'

    fechaInscripcion = fields.Datetime(string='Fecha Inscripción', required=True, default=lambda self: fields.datetime.now())
    cicloescolaridad_id = fields.Many2one('escuela.cicloescolaridad', inverse_name='inscripcion_ids', string='Ciclo de Escolaridad')
    alumno_id = fields.Many2one('escuela.alumno', inverse_name='inscripcion_ids', string='Alumno')