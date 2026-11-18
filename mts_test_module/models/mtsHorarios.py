from odoo import fields, models
from odoo.tools.float_utils import *

class MTSHorarios(models.Model):
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
        required=True,
        default="0",
    )
    from_hour = fields.Float(string="Desde", required=True)
    to_hour = fields.Float(string="Hasta", required=True)

    client_id = fields.Many2one(
        "res.partner",
    )

    #_check_schedule = models.Constraint(
    #    'CHECK(from_hour < to_hour)',
    #    'From_hour can\'t be larger or equal to To_hour.'
    #)

    @api.constrains("from_hour", "to_hour")
    def _check_schedule(self):
        for record in self:
            if float_compare(record.from_hour, record.to_hour, precision_digit=6)  >= 0:
                return ValidationError("From_hour can't be larger or equal to To_hour")


