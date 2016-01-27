# -*- coding: utf-8 -*-

from datetime import timedelta
from openerp import models, fields, api, exceptions

class hrproject(models.Model):
    _name = 'hr.analytic.timesheet'
    _inherit = 'hr.analytic.timesheet'

    work_ids = fields.Many2one('project.task.work','hr_analytic_timesheet_id', String="Works")
