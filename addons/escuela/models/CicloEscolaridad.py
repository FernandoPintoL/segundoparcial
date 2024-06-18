# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CicloEscolaridad(models.Model):
    _name = 'escuela.cicloescolaridad'
    _description = 'escuela.cicloescolaridad'

    name = fields.Char(string="Detalle", compute='_compute_name', store=True)
    anioEscolaridad = fields.Selection([
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('tercero', 'Tercero'),
        ('cuarto', 'Cuarto'),
        ('quinto', 'Quinto'),
        ('sexto', 'Sexto'),
    ], string='Año de Escolaridad', required=True)
    nivel = fields.Selection([
        ('inicial', 'Inicial'),
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
    ], string='Nivel', required=True)
    paralelo = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ], string='Paralelo', required=True)
    aula_id = fields.Many2one('escuela.aula', string='Aula', inverse_name='cicloescolaridad_ids')
    gestionacademica_id = fields.Many2one('escuela.gestionacademica', inverse_name='cicloescolaridad_ids', string='Gestion Academica')
    inscripcion_ids = fields.One2many('escuela.inscripcion', inverse_name='cicloescolaridad_id',string='Inscripcion')
    horario_ids = fields.One2many('escuela.horario', inverse_name='cicloescolaridad_id',string='Horario')
    
    @api.depends('anioEscolaridad', 'nivel', 'paralelo')
    def _compute_name(self):
        for record in self:
            record.name = "Ciclo: "+str(record.anioEscolaridad)+" "+str(record.paralelo)
    
    