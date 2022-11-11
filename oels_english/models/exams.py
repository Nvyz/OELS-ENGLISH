from odoo import api, fields, models


class Exams(models.Model):
   _name = "oels.exams"
   _inherit = "mail.thread"
   _description = "Exams"
   _rec_name = "student"


   id = fields.Char(string='id')
   type = fields.Selection([
       ('Writing', 'Writing'),
       ('Reading', 'Reading'),
       ('Listening', 'Listening'),
       ('Speaking', 'Speaking'),
       ('Grammar and Vocabulary', 'Grammar and Vocabulary'),
   ], required=True, default='Grammar and Vocabulary')
   student = fields.Many2one('oels.students',string='Student', required=True, tracking=True)
   grade = fields.Char(string='Grade',tracking=True)
   date = fields.Date('Exam date',tracking=True)
   annotations = fields.Text('Annotations')

