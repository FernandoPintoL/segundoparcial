from odoo import fields, models, api

class Edificio(models.Model):
    _name = 'escuela.edificio'
    _description = 'escuela.edificio'
    
    name = fields.Char(string='Nombre', required=True, unique=True)
    nropiso = fields.Integer(string='Nuros de Pisos')
    fecha_construccion = fields.Date(string='Fecha de Construcción')
    colegio_id = fields.Many2one('escuela.colegio', inverse_name='edificio_ids', string='Colegio')
    aula_ids = fields.One2many('escuela.aula', inverse_name='edificio_id', string='Aulas')