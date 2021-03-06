# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Multi Company Security",
    "summary": """
        This module modifies the access rules for 
        multi-company. 
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["PerezGabriela"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "11.0.1.0.0",
    "depends": [
        "account_asset",
        "account_check",
        "analytic",
        "crm",
        "date_range",
        "hr",
        "l10n_ar_account_withholding",
        "l10n_ar_account_vat_ledger",
        "mrp",
        "purchase",
        "report_extended",
        "sale",
    ],
    'data': [
        'security/multi_company_security.xml',
    ],
}
