from odoo import fields, models, api
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError

class MTSHorarios(models.Model):
    _name = "mts.horarios"

    from_hour = fields.Float(string="Desde", required=True)
    to_hour = fields.Float(string="Hasta", required=True)

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

    client_id = fields.Many2one(
        "res.partner",
    )

    _check_schedule = models.Constraint(
        'CHECK(from_hour < to_hour)',
        'From_hour can\'t be larger or equal to To_hour.'
    )

    _check_bounds = models.Constraint(
        'CHECK(to_hour <= 24)',
        'To_hour can\'t be greater than 24'    
    )   

    @api.constrains("day", "from_hour", "to_hour")
    def _check_schedule(self):

        for record in self:

            overlap = self.search(
                [
                    ("id", "!=", record.id),
                    ("day", "==", record.day),
                    ("from_hour", "<", record.to_hour),
                    ("to_hour", ">", record.from_hour)
                ]
            )

            if overlap:
                raise ValidationError("There are overlapping schedules")



