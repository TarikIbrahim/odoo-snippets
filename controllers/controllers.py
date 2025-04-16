# -*- coding: utf-8 -*-
# from odoo import http


# class Dynamic-column-label(http.Controller):
#     @http.route('/dynamic-column-label/dynamic-column-label', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dynamic-column-label/dynamic-column-label/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dynamic-column-label.listing', {
#             'root': '/dynamic-column-label/dynamic-column-label',
#             'objects': http.request.env['dynamic-column-label.dynamic-column-label'].search([]),
#         })

#     @http.route('/dynamic-column-label/dynamic-column-label/objects/<model("dynamic-column-label.dynamic-column-label"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dynamic-column-label.object', {
#             'object': obj
#         })
