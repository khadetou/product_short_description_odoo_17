from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    description_short = fields.Text(
        string="Short Description",
        translate=True,
        help="A shorter description of the product that will be displayed on quotations and invoices.",
    )
