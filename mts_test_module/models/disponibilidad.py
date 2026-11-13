from odoo import fields, models

class disponibilidad(models.Model):
    _name = "mts.horarios"

    client_id = fields.Many2One(
        "res.partner",
        string="Partners"
    )


