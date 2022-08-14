import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'pm.lib.book'
    _description = 'Book'

    name = fields.Char()
    isbn = fields.Char()
    author = fields.Many2many(
        comodel_name='pm.lib.author',
    )
