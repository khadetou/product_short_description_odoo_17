from odoo import models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def _get_computed_name(self):
        """Override to use short description if available"""
        self.ensure_one()
        if (
            self.product_id
            and self.product_id.description_short
            and self.move_id.move_type in ("out_invoice", "out_refund")
        ):
            return self.product_id.description_short
        return super()._get_computed_name()
