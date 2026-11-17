{
    "name": "Test module",
    "summary": "it does nothing",
    "description": """
        it does nothing
    """,
    "version": "19.0.1.0.0",
    "author": "MTS",
    "website": "https://www.madetosoft.com",
    "license": "LGPL-3",
    "category": "Custom",
    "depends": [
    "base",
    "contacts"
    ],
    "data": [ 
        "security/ir.model.access.csv",
        "views/custom_partner_view.xml",
        "views/crm_view_parner.xml",
        "views/custom_views.xml"
    ],
    "installable": True,
    "application": False,
}