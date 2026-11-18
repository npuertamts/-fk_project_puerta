from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    company_name = fields.Char(string="Nombre Comercial empresa")
    company_date = fields.Date(string="Fecha Creación empresa")
    x_company_facturation = fields.Float(string="Facturación empresa")

    horario_ids = fields.One2many(
        "mts.horarios",
        "client_id",
        string="horarios"
    )   