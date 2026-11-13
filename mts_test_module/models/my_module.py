from odoo import models, fields, api


class my_modul(models.Model):
    _inherit = "res.partner"

    company_name = fields.Char(string="Nombre Comercial empresa")