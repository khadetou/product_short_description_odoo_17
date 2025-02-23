from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_sale_order_line_multiline_description_sale(self):
        """Override to use short description if available"""
        self.ensure_one()
        if self.product_id.description_short:
            return self.product_id.description_short
        return super()._get_sale_order_line_multiline_description_sale()
