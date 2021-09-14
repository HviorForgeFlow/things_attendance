{
    "name": "Things Gateway",
    "summary": "Connect your Gateways with Odoo",
    "version": "14.0.1.0.0",  # update controllers.main.ThingsRasGate
    "category": "Things",
    "website": "https://github.com/thingsintouch/things-odoo-addons",
    "images": [
        "static/description/icon.png",
    ],
    "author": "thingsintouch.com",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base"],
    "data": [
        "security/things_ras_security.xml",
        "security/ir.model.access.csv",
        "views/things_menus.xml",
        "views/things_ras2.xml",
    ],
    # 'demo': ['demo.xml'],
}
