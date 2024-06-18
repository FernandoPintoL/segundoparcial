from odoo import fields, models

class Mensualidad(models.Model):
    _name = 'escuela.mensualidad'
    _description = 'escuela.mensualidad'

    monto= fields.Float(string='Monto', required=True)
    detalle= fields.Char(string='Detalle')
    fechaPago= fields.Datetime(string='Fecha Pago', default=lambda self: fields.datetime.now())
    tutor_id = fields.Many2one('escuela.tutor', inverse_name='mensualidad_ids', string='Tutor')
    gestionacademica_id = fields.Many2one('escuela.gestionacademica', inverse_name='mensualidad_ids', string='Gestion Academica')