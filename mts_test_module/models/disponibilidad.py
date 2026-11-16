from odoo import fields, models

class disponibilidad(models.Model):
    _name = "mts.horarios"
    day = fields.Selection(
        string="Day",
        selection=[
                   ("0", "Lunes"),
                   ("1", "Martes"),
                   ("2", "Miercoles"),
                   ("3", "Jueves"),
                   ("4", "Viernes"),
                   ("5", "Sabado"),
                   ("6", "Domingo")
                   ],
        required=True
    )
    from_hour = fields.Datetime(string="Desde", required=True)
    to_hour = fields.Datetime(string="Hasta", required=True)

    client_id = fields.Many2one(
        "res.partner",
    )   


