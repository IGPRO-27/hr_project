# -*- coding: utf-8 -*-
#from datetime import timedelta
from openerp import models, fields, api, exceptions

class hrproject(models.TransientModel):
    _name = 'hr.sheet.wizard'
    # _inherit = 'hr.analytic.timesheet

    sheet_id =  fields.Many2one("hr_timesheet_sheet.sheet", string="Sheets", required=True)
    description = fields.Char(string ="Description" ,  required=True)
    Task_ids = fields.Many2one("project.task",string="Tache",required=True)
    hour = fields.Float(string="Time Spent" , required=True)
    work_ids =  fields.Many2one("project.task.work", string="Works")


    @api.one
    def save(self):
        # self.work_ids.display_name=self.description
        # self.work_ids.hours=self.hour
        # self.work_ids.task_id=self.Task_ids

        #call create function
        record = self.env['project.task.work'].create({
            'name':self.description,
            'hours':self.hour,
            'task_id':self.Task_ids.id,
            })

        #self.sheet_id.timesheet_ids |= self.work_ids.hr_analytic_timesheet_id
        return res_id

    # TypeError: cannot convert dictionary update sequence element #0 to a sequence

    # work_ids = fields.Many2one('project.task.work','hr_analytic_timesheet_id', String="Works")

    # _sql_constraints = [
    #     ('work_ids_constraint',
    #      'unique(work_ids)',
    #      'Choose another value - it has to be unique! please check your work')
    # ]

    # def _auto_init(self, cr, context=None):
    #     self._sql_constraints = self._sql_constraints.reverse()
    #     super(hrproject, self)._auto_init(cr, context)

# class hrinheritsproject(models.Model):
#     _name = 'hr.analytic.timesheet.delegate'
#     _inherits = {'hr.analytic.timesheet':'work_ids'}

#     work_ids = fields.Many2one('project.task.work','hr_analytic_timesheet_id', String="Works", auto_join=True)



    # @api.model
    # def create(self, work_ids):
    #     record = super(hrproject, self).create(work_ids)
    #     print record
    #     return record

    # @api.one
    # @api.constrains(work_ids)
    # def _work_unique(self):
    #     if self == self.work_ids:
    #         raise exceptions.ValidationError("ID not unique")
