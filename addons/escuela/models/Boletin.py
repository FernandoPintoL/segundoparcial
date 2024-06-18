from odoo import models, fields, api

class Boletin(models.Model):
    _name = 'escuela.boletin'
    _description = "escuela.boletin"
    
    alumno_id = fields.Many2one('escuela.alumno', string='Alumno')
    alumno_nombre = fields.Char('Nombre del Alumno')
    alumno_ci = fields.Char('CI del Alumno')
    asignatura = fields.Char('Asignatura')
    nota = fields.Float('Nota')
    estado = fields.Char('Estado')
    
    
    @api.model
    def init(self):
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW boletin AS (
                SELECT
                    row_number() OVER () AS id,
                    a.id AS alumno_id,
                    a.name AS alumno_nombre,
                    a.ci AS alumno_ci,
                    asig.name AS asignatura,
                    n.nota,
                    n.estado
                FROM
                    escuela.notasasignatura n
                JOIN
                    escuela.alumno a ON n.alumno_id = a.id
                JOIN
                    escuela.asignatura asig ON n.asignatura_id = asig.id
                ORDER BY
                    a.nombre,
                    asig.nombreAsignatura
            )
        """)