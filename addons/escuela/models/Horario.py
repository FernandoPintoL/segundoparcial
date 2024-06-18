from odoo import fields, models

class Horario(models.Model):
    _name = 'escuela.horario'
    _description = 'escuela.horario'

    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miercoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sabado'),
        ('domingo', 'Domingo'),
    ], string='Día', required=True)
    inicio_datetime = fields.Datetime(string='Hora Inicio', required=True)
    final_datetime = fields.Datetime(string='Hora Final', required=True)
    asignatura_id = fields.Many2one('escuela.asignatura', inverse_name='horario_ids',string='Asignatura')
    cicloescolaridad_id = fields.Many2one('escuela.cicloescolaridad', inverse_name='horario_ids',string='Ciclo de Escolaridad')
    profesor_id = fields.Many2one('escuela.profesor', inverse_name='horario_ids', string='Profesor')
    alumno_id = fields.Many2one('escuela.alumno', inverse_name='horario_ids', string='Alumno')
    user_id = fields.Many2one('res.users', string='User de registro', required=True, default=lambda self: self.env.user)
    