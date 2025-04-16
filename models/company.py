from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'
    
    company_karat_type = fields.Char(string='Company Karat Type')

