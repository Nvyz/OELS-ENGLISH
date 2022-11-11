from odoo import api, fields, models


class Reminders(models.Model):
   _name = "oels.reminders"
   _inherit = "mail.thread"
   _description = "Reminders"
   _rec_name = "student"

   def action_done(self):
       self.state="done"

   def action_progress(self):
       self.state = "progress"

   def action_cancelled(self):
       self.state = "cancelled"


   id = fields.Char(string='id')
   student = fields.Many2one('oels.students',string='Student', required=True, tracking=True)
   name = fields.Char('Title', help='Reminder name')
   date = fields.Date('Date', help='Reminder date')
   description = fields.Text('Description',
                              help='Description of the reminder')
   state = fields.Selection([('done', 'Done'),('progress','In Progress'),('cancelled','Cancelled')], default='progress', string="Status",tracking=True)
