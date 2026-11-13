from odoo import models, fields, api


class my_modul(models.Model):
    _name = "Contact"

    company_name = fields.Text()