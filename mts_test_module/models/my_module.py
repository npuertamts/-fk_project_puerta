from odoo import models, fields, api


class my_modul(models.Model):
    _name = "my_module.my_module"

    company_name = fields.Text()