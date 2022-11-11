from odoo import api, fields, models
import datetime

class Classes(models.Model):
   _name = "oels.groups"
   _inherit = "mail.thread"
   _description = "Groups"
   _rec_name = "classname"

   id = fields.Char(string='id')
   type = fields.Selection([
      ('A1', 'A1'),
      ('A2', 'A2'),
      ('B1', 'B1'),
      ('B2', 'B2'),
      ('C1', 'C1'),
      ('C2', 'C2'),
   ], required=True, default='B2')
   schedule_start = fields.Char(string='Schedule start', required=True, tracking=True)
   schedule_end = fields.Char(string='Schedule end', required=True, tracking=True)
   teacher = fields.Many2one('oels.employees',string='Teacher', required=True, tracking=True)
   student_id = fields.One2many('oels.students', 'groupid', string="Students")
   classname = fields.Char(string='Class Name', required=True,tracking=True)

