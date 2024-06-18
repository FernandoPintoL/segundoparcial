from odoo import models, fields 

class GestionAcademica(models.Model):
    _name = 'escuela.gestionacademica'
    _description = 'escuela.gestionacademica'

    name = fields.Char(string='Detalle')
    gestionPeriodo = fields.Char(string='Año de Gestion', required=True)
    fechaInicial = fields.Date(string='Fecha Inicial', required=True, default=lambda self: fields.datetime.today())
    fechaFinal = fields.Date(string='Fecha Final', required=True, default=lambda self: fields.datetime.today())
    modoEvaluacion = fields.Selection([
        ('bimestral', 'Bimestral'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
    ], string='Modo Evaluacion', required=True)
    # fechaHoraCreacion = fields.Datetime(string='Fecha Hora Creacion', default=fields.Datetime.now())
    cicloescolaridad_ids = fields.One2many('escuela.cicloescolaridad', inverse_name='gestionacademica_id',string='Ciclo de Escolaridad')
    mensualidad_ids = fields.One2many('escuela.mensualidad', inverse_name='gestionacademica_id',string='Mensualidades')