# -*- coding: utf-8 -*-
# from odoo import http


# class Template(http.Controller):
#     @http.route('/template/template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/template/template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('template.listing', {
#             'root': '/template/template',
#             'objects': http.request.env['template.template'].search([]),
#         })

#     @http.route('/template/template/objects/<model("template.template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('template.object', {
#             'object': obj
#         })
