from odoo import fields, models

class Aula(models.Model):
    _name = 'escuela.aula'
    _description = 'escuela.aula'

    name = fields.Char(string='Nombre', required=True, unique=True)
    capacidad = fields.Integer(string='Capacidad')
    tipo = fields.Selection([
        ('clases', 'Clases Normales'),
        ('administrativo', 'Administrativo'),
        ('tecnica', 'Ramas Tecnicas')
    ], string='Tipo de Aula', required=True)
    area = fields.Float(string='Área')
    edificio_id = fields.Many2one('escuela.edificio', inverse_name='aula_ids', string='Edificio')
    recurso_ids = fields.One2many('escuela.recurso', inverse_name='aula_id', string='Recursos')
    cicloescolaridad_ids = fields.One2many('escuela.cicloescolaridad', inverse_name='aula_id', string='Ciclo de escolaridad')
