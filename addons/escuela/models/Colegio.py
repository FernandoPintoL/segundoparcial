# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Colegio(models.Model):
    _name = 'escuela.colegio'
    _description = 'escuela.colegio'

    name = fields.Char(string='Unidad Educativa', required=True, unique=True)
    departamento = fields.Selection([
        ('santacruz', 'Santa Cruz'),
        ('beni', 'Beni'),
        ('cochabamba', 'Cochabamba'),
        ('chuquisaca', 'Chiquisaca'),
        ('pando', 'Panda'),
        ('lapaz', 'La Paz'),
        ('oruro', 'Oruro'),
        ('potosi', 'Potosí'),
        ('tarija', 'Tarija'),
    ], string='Departamento', required=True)
    direccion_distrital = fields.Selection([
        ('distrito1', 'Distrito 1'),
        ('distrito2', 'Distrito 2'),
        ('distrito3', 'Distrito 3'),
        ('distrito4', 'Distrito 4'),
        ('distrito5', 'Distrito 5'),
        ('distrito6', 'Distrito 6'),
        ('distrito7', 'Distrito 7'),
        ('distrito8', 'Distrito 8'),
        ('distrito9', 'Distrito 9'),
        ('distrito10', 'Distrito 10'),
        ('distrito11', 'Distrito 11'),
        ('distrito12', 'Distrito 12'),
        ('distrito13', 'Distrito 13'),
        ('distrito14', 'Distrito 14'),
        ('distrito15', 'Distrito 15'),
        ('otro', 'Otro'),
    ], string='Direccion Distrital', required=True)
    sie = fields.Char(string='SIE', required=True, unique=True)
    director = fields.Char(string='Director', required=True, unique=True)
    turno = fields.Selection([
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche')
    ], string='Turno', required=True)
    edificio_ids = fields.One2many('escuela.edificio', inverse_name='colegio_id', string='Edificio')
    instalacionescomunes_ids = fields.One2many('escuela.instalacionescomunes', inverse_name='colegio_id', string='Instalaciones Comunes')
    
    
    