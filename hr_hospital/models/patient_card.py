import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class PatientCard(models.Model):
    _name = 'pm.patient.card'
    _description = 'Patient card'

    name = fields.Char()
    doctors = fields.Many2many(comodel_name='pm.doctor')
    diagnosis = fields.Many2many(comodel_name='pm.diagnosis')
    prescription = fields.Char()
