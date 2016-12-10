# -*- coding: utf-8 -*-
from odoo import http

# class Redfactory(http.Controller):
#     @http.route('/redfactory/redfactory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/redfactory/redfactory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('redfactory.listing', {
#             'root': '/redfactory/redfactory',
#             'objects': http.request.env['redfactory.redfactory'].search([]),
#         })

#     @http.route('/redfactory/redfactory/objects/<model("redfactory.redfactory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('redfactory.object', {
#             'object': obj
#         })