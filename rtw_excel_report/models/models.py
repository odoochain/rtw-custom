# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rtw_excel_report(models.Model):
#     _name = 'rtw_excel_report.rtw_excel_report'
#     _description = 'rtw_excel_report.rtw_excel_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
