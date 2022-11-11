from odoo import api, fields, models


class Students(models.Model):

   _name = "oels.students"
   _description = "Students"
   _inherit = "mail.thread"
   _rec_name="name"


   id = fields.Char(string='id')
   name = fields.Char(string='Full Name', required=True, tracking=True)
   age = fields.Date(string='Date of Birth', tracking=True)
   gender = fields.Selection([
      ('male', 'Male'),
      ('female', 'Female'),
      ('other', 'other'),
   ], required=True, default='male')
   in_person = fields.Selection([
      ('Yes', 'Yes'),
      ('No', 'No'),
   ], required=True, default='Yes')
   adress = fields.Char(string='Adress', required=True, tracking=True)
   phone = fields.Char(string='Phone', required=True, tracking=True)
   email = fields.Char(string='Email', required=True, tracking=True)
   teacher = fields.Many2one('oels.employees',string='Teacher', required=True, tracking=True)
   groupid = fields.Many2one('oels.groups',string='Group', required=True, tracking=True)
   registration_date = fields.Date(string='Registration Date', tracking=True)
   state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status",
                            tracking=True)
   notes = fields.Text(string='Notes')
   image = fields.Binary(string="Photo")
   grades_id = fields.One2many('oels.exams', 'student',
                                           string="Grades", required=True, tracking=True)
   reminders_id = fields.One2many('oels.reminders', 'student',
                                           string="Reminders", required=True, tracking=True)




