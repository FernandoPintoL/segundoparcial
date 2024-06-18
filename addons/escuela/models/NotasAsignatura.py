from odoo import fields, models, api

class NotasAsignatura(models.Model):
    _name = 'escuela.notasasignatura'
    _description = 'escuela.notasasignatura'

    nota = fields.Float(string='Nota', required=True, default=100)
    estado = fields.Selection([
        ('aprobado', 'Aprobado'),
        ('reforzamiento', 'Reforzamiento'),
        ('reprobado', 'Reprobado'),
    ], string='Estado', compute='_compute_estado', store=True, default="aprobado")
    alumno_id = fields.Many2one('escuela.alumno', inverse_name='notasasignatura_ids', string='Alumno')
    asignatura_id = fields.Many2one('escuela.asignatura', inverse_name='notasasignatura_ids', string='Asignatura Materia')
    
    @api.depends('nota')
    def _compute_estado(self):
        for record in self:
            if record.nota >= 60:
                record.estado = 'aprobado'
            elif record.nota >= 45 and record.nota <= 59:
                record.estado = 'reforzamiento'
            else:
                record.estado = "reprobado"