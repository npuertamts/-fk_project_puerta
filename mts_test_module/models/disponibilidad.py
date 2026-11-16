from odoo import fields, models

class disponibilidad(models.Model):
    _name = "mts.horarios"
    from_hour = fields.Float(string="Desde", required=True)
    to_hour = fields.Float(string="Hasta", required=True)

    client_id = fields.Many2one(
        "res.partner",
        string="Partners"
    )   


