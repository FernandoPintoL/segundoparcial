# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Escuela(http.Controller):
    @http.route('/escuela/horario', auth='public',  website=True)
    def index(self, **kw):
        records = request.env['escuela.horario'].search([])
        # return request.render('view_gestion_horario.template', {
        #     'records': "HOLA WORLD",
        # })
        return "Hello, world"

#     @http.route('/escuela/escuela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuela.listing', {
#             'root': '/escuela/escuela',
#             'objects': http.request.env['escuela.escuela'].search([]),
#         })

#     @http.route('/escuela/escuela/objects/<model("escuela.escuela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuela.object', {
#             'object': obj
#         })