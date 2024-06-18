from odoo import models, fields, api

class StudentReport(models.Model):
    _name = 'student.report'
    _description = "Student Report"
    _auto = False
    
    # alumno_id = fields.Many2one('escuela.alumno', string='Alumno')
    # alumno_nombre = fields.Char('Nombre del Alumno')
    # alumno_ci = fields.Char('CI del Alumno')
    # asignatura = fields.Char('Asignatura')
    # nota = fields.Float('Nota')
    # estado = fields.Char('Estado')
    
    @api.model
    def _get_report_values(self, docids, data=None):
        # Ejecuta tu consulta SQL aquí
        self.env.cr.execute("""
            SELECT row_number() OVER () AS id,
                    a.id AS alumno_id,
                    a.name AS alumno_nombre,
                    a.ci AS alumno_ci,
                    asig.name AS asignatura,
                    n.nota,
                    n.estado
                 FROM
                    escuela_notasasignatura n
                 JOIN
                    escuela_alumno a ON n.alumno_id = a.id
                 JOIN
                    escuela_asignatura asig ON n.asignatura_id = asig.id
                 ORDER BY
                    a.name,
                    asig.name
        """)
        result = self.env.cr.fetchall()
        
        # Procesa los resultados y prepáralos para la plantilla
        docs = [{'field1': row[0], 'field2': row[1]} for row in result]
        
        return {
            'doc_ids': docids,
            'doc_model': 'your.model',
            'docs': docs,
            'other_data': data,
        }
    
    # @api.model
    # def init(self):
        # self.env.cr.execute("""
        #     CREATE OR REPLACE VIEW student_report AS (
        #         SELECT
        #             row_number() OVER () AS id,
        #             a.id AS alumno_id,
        #             a.name AS alumno_nombre,
        #             a.ci AS alumno_ci,
        #             asig.name AS asignatura,
        #             n.nota,
        #             n.estado
        #         FROM
        #             escuela_notasasignatura n
        #         JOIN
        #             escuela_alumno a ON n.alumno_id = a.id
        #         JOIN
        #             escuela_asignatura asig ON n.asignatura_id = asig.id
        #         ORDER BY
        #             a.name,
        #             asig.name
        #     )
        # """)
        # result = self.env.cr.dictfetchall()
        # for row in result:
        #     self.create(row)