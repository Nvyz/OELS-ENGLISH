# -*- coding: utf-8 -*-
from odoo import api, fields, models
import sys
from odoo.exceptions import UserError



class OelsEmployees(models.Model):
   _name = "oels.employees"
   _inherit = "mail.thread"
   _description = "Employees"
   _rec_name="name"
   sys.setrecursionlimit(1500)


   def action_confirm(self):
       self.state = 'confirm'
   def action_done(self):
       self.state="done"
   def action_draft(self):
       self.state="draft"
   def action_cancel(self):
       self.state="cancel"


   id = fields.Integer(string='id')
   name = fields.Char(string='Full name', required=True, tracking=True)
   age = fields.Date(string='Date of Birth', tracking=True)
   gender = fields.Selection([
     ('male','Male'),
     ('female','Female'),
     ('other', 'other'),
   ], required=True, default='male')
   adress = fields.Char(string='Adress', required=True, tracking=True)

   phone = fields.Char(string='Phone', required=True, tracking=True)

   email = fields.Char(string='Email', required=True, tracking=True)

   groups_id = fields.One2many('oels.groups', 'teacher',
                                           string="Groups")
   students_id = fields.One2many('oels.students', 'teacher',
                                           string="Students")
   image = fields.Binary(string="Photo")

   start_date = fields.Date(string='Start Date', tracking=True)
   @api.constrains('phone')
   def check_phone(self):
       if len(self.phone) < 9 or len(self.phone) > 9:
           raise UserError("Phone field must have 9 digits")
       if not self.phone.isdigit():
           raise UserError("Phone field must be numeric")


   @api.constrains('age')
   def _compute_student_age(self):
       current_dt = fields.Date.today()
       if self.age > current_dt:
           raise UserError("Date is invalid")
       age_calc = ((current_dt - self.age).days / 365)
       if age_calc<18:
           raise UserError("You need to be 18 at least!")













