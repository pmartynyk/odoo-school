import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)

class Doctor(models.Model):
    _name = 'pm.doctor'
    _description = 'Doctor'

    name = fields.Char()
