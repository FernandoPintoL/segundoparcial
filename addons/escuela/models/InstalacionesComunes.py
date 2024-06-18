from odoo import models, fields, api

class InstalacionesComunes(models.Model):
    _name = 'escuela.instalacionescomunes'
    _description = 'escuela.instalacionescomunes'

    name = fields.Char(string='Nombre', required=True)
    capacidad = fields.Integer(string='Capacidad de Personas')
    colegio_id = fields.Many2one('escuela.colegio', inverse_name='colegio_ids', string='Colegio')