# -*- coding: utf-8 -*-

from datetime import timedelta
from openerp import models, fields, api, exceptions

class hrproject(models.Model):
    _name = 'hr.analytic.timesheet'
    _inherit = 'hr.analytic.timesheet'

    work_ids = fields.Many2many('project.task.work', String="Works")
