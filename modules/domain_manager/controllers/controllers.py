# -*- coding: utf-8 -*-
# from odoo import http


# class DomainManager(http.Controller):
#     @http.route('/domain_manager/domain_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/domain_manager/domain_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('domain_manager.listing', {
#             'root': '/domain_manager/domain_manager',
#             'objects': http.request.env['domain_manager.domain_manager'].search([]),
#         })

#     @http.route('/domain_manager/domain_manager/objects/<model("domain_manager.domain_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('domain_manager.object', {
#             'object': obj
#         })
