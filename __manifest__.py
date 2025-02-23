{
    "name": "Product Short Description",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "summary": "Add short description field to products and enhance quote/invoice display",
    "description": """
        This module adds a short description field to products and enhances the display of products in:
        * Product views
        * Sales quotations
        * Customer invoices
        Including product images in a clean layout.
    """,
    "depends": [
        "product",
        "sale",
        "account",
    ],
    "data": [
        "views/product_views.xml",
        "report/sale_report_templates.xml",
        "report/account_report_templates.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
