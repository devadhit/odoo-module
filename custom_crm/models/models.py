# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class CrmProduct(models.Model):
    _name = 'crm.product'
    _description = 'CRM Product'

    product_id = fields.Many2one('crm.product', 'Product')
    name = fields.Char('Nama Produk')

class custom_crm(models.Model):
    _inherit = 'crm.lead'

    is_pelangganbaru = fields.Boolean('Pelanggan Baru')
    segment = fields.Selection([
        ('kontruksi', 'Kontruski'),
        ('perbankan', 'Perbankan'),
        ('pemerintah', 'Pemerintah'),
        ('bumdbumn', 'BUMD/BUMN'),
        ('kementrian', 'Kementrian'),
        ('swasta', 'Swasta Lainnya')
    ], string='Segment Pelanggan')
    
    product_ids = fields.One2many('crm.product', 'product_id', string='Product')
   

    
    