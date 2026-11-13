from odoo import models, fields, api


class my_modul(models.Model):
    _inherit = "res.partner"

    company_name = fields.Char(string="Nombre Comercial empresa")
    company_date = fields.Date(string="Fecha Creación empresa")
    company_fac = fields.Float(string="Facturación empresa")