from odoo import fields, models

class Recurso(models.Model):
    _name = 'escuela.recurso'
    _description = 'escuela.recurso'

    name = fields.Char(string='Nombre', required=True)
    tipo_recurso = fields.Char(string='Tipo de Recurso')
    cantidad = fields.Integer(string='Cantidad')
    aula_id = fields.Many2one('escuela.aula', inverse_name='recurso_ids', string='Aula')
