# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    """
    Extends Employee model to manage Payroll details
    without requiring hr_contract.
    """

    _inherit = "hr.employee"
    _description = "Employee Payroll Settings"

    payroll_struct_id = fields.Many2one(
        "hr.payroll.structure",
        string="Salary Structure",
    )

    schedule_pay = fields.Selection(
        [
            ("monthly", "Monthly"),
            ("quarterly", "Quarterly"),
            ("semi-annually", "Semi-annually"),
            ("annually", "Annually"),
            ("weekly", "Weekly"),
            ("bi-weekly", "Bi-weekly"),
            ("bi-monthly", "Bi-monthly"),
        ],
        string="Scheduled Pay",
        index=True,
        default="monthly",
        help="Defines the frequency of the wage payment.",
    )

    resource_calendar_id = fields.Many2one(
        "resource.calendar",
        string="Working Schedule",
        required=False,  # relaxed requirement since no contract
        help="Employee's working schedule.",
    )

    def get_all_structures(self):
        """
        @return: the structures linked to the employee, ordered by
                 hierarchy (parent=False first, then children, etc.)
                 and without duplicates.
        """
        return self.payroll_struct_id.get_structure_with_parents()

