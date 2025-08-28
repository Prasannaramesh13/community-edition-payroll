# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    "name": "community_edition_payroll",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "license": "LGPL-3",
    "summary": "Manage employee payroll, contracts, and payslips in Odoo Community Edition",
    "description": """
HR Payroll Community Edition
============================

This module allows you to manage employee payroll in Odoo Community Edition.

Features:
---------
- Manage payroll records
- Create and manage employee contracts with salary structure
- Generate employee payslips
- Payroll reports and contribution registers
- Works with Odoo HR & Leaves (hr, hr_holidays)
    """,
    "author": "BrowseInfo, Odoo Community Association (OCA)",
    "website": "https://www.browseinfo.com",
    "depends": [
        "hr",
        "hr_holidays",
    ],
    "data": [
        "security/ir.model.access.csv",   # access rights first
        "data/hr_payroll_sequence.xml",
        "data/hr_payroll_data.xml",
        "wizard/hr_payroll_payslips_by_employees_views.xml",
        "wizard/hr_payroll_contribution_register_report_views.xml",
        "views/hr_contract_views.xml",
        "views/hr_salary_rule_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_employee_views.xml",
        "views/hr_employee_payroll_views.xml",
        "views/res_config_settings_views.xml",
        "views/hr_payroll_report.xml",
        "views/report_contributionregister_templates.xml",
        "views/report_payslip_templates.xml",
        "views/report_payslipdetails_templates.xml",
        "security/hr_payroll_security.xml",  # security rules last (needs models)
    ],
    "demo": ["data/hr_payroll_demo.xml"],
    "application": True,
    "installable": True,
    "auto_install": False,
    "images": ["static/description/Banner.gif"],
}
