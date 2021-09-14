# Copyright 2017 Comunitea Servicios Tecnológicos S.L.
# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# Copyright 2021 http://www.thingsintouch.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Things RAS3",
    "summary": "Connect Odoo with your RFID Attendance Terminal RAS3",
    "version": "14.0.1.0.0",
    "category": "Things",
    "website": "https://github.com/thingsintouch/things-odoo-addons",
    "author": "Comunitea,"
    "Eficent,"
    "Odoo Community Association (OCA)"
    "thingsintouch.com",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_attendance",
        "things_gateway",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_view.xml",
        "wizard/add_singleton.xml",
        "views/res_config_settings_views.xml",
    ],
}
