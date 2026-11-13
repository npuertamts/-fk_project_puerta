from odoo import fields, models

class disponibilidad(models.Model):
    _name = "mts.horarios"

    client_id = fields.Many2one(
        "res.partner",
        string="Partners"
    )


