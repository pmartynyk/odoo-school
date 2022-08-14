import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class author(models.Model):
    _name = 'pm.lib.author'
    _description = 'Author'

    name = fields.Char()
