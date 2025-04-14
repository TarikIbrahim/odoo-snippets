from odoo import models, fields, api
class Company(models.Model):
    _inherit = 'res.comany'
    
    company_karat_type = filds.Char(string='Company Karat Type')

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    company_karat_weight = fields.Float(string='Weight', store=True)  # Your existing field
    company_karat_type = fields.Char(string='Karat Type')  # Your existing field
    
    @api.model
    def fields_get(self, allfields=None, attributes=None):
        """Override fields_get to dynamically change the field's string"""
        res = super().fields_get(allfields=allfields, attributes=attributes)
        
        if 'company_karat_weight' in res:
            # You may need to check allowed user companies in case of multi-company
            company = self.env.company
            karat_type = getattr(company, 'company_karat_type', 'K24')  # Default to K24 if not set
            res['company_karat_weight']['string'] = f'Weight ({karat_type})'
            
        return res
