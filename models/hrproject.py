# -*- coding: utf-8 -*-
#from datetime import timedelta
from openerp import models, fields, api, exceptions

class hrproject(models.TransientModel):
    _name = 'hr.sheet.wizard'

   # user_id = fields.Many2one('res.users', 'user', required=True)
    sheet_id =  fields.Many2one("hr_timesheet_sheet.sheet", string="Sheets", required=True)
    description = fields.Char(string ="Description" ,  required=True)
    Task_ids = fields.Many2one("project.task", string="Tache", required=True)
    hour = fields.Float(string="Time Spent" , required=True)
    work_ids =  fields.Many2one("project.task.work", string="Works")

    # def create(self,cr, uid, context=None, user_id)

    # if context is None:context ={}
    # model_name=context.get('active_model')
    #     emp_obj = self.pool.get('hr.employee')
    #     emp_id = emp_obj.search(cr, uid, [('user_id', '=', user_id)])
        # print "L'UTILISATEUR EST %s " %(emp_id.name)

    @api.multi
    def save(self):

       # emp_obj = self.pool.get('hr.employee')
       # emp_id = self.env('hr.employee').search([('user_id', '=',self.user_id)])
        print "--------------------------------------------"
        print self.env.uid

        # self.work_ids.display_name=self.description
        # self.work_ids.hours=self.hour
        # self.work_ids.task_id=self.Task_ids

        # uid=self._uid
        # print "--------------------------------------------"
        # print uid
        # ids=self._ids
        # print "--------------------------------------------"
        # print ids
        # context=self._context
        # print "--------------------------------------------"
        # print context
        # # cr=self._cr.fetchone()[0]

        # # print "--------------------------------------------"
        # # print cr

        # if context is None: context = {}

        # active_id  = context.get('active_id',False)

        self.env['project.task.work'].create({
            'name':self.description,
            'hours':self.hour,
            'task_id':self.Task_ids.id,
            'user_id':self.env.uid,
            })
        return {}

       #self.sheet_id.timesheet_ids |= self.work_ids.hr_analytic_timesheet_id
       # return {}
