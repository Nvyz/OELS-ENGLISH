# -*- coding: utf-8 -*-
{
'name': 'OELS English',
'description': 'English Academy',
'author': 'Hugo Pires Rodríguez',
'sequence':-100,
'depends': [
       'base',
       'mail'
      ],
'data':[
 'data/data.xml',
 'security/ir.model.access.csv',
 'views/employees.xml',
 'views/groups.xml',
 'views/students.xml',
 'views/reminder.xml',
 'views/exams.xml',
 'report/employee_details.xml',
 'report/employee_details_and_groups.xml',
 'report/employee_details_and_students.xml',
 'report/report.xml'
],
'demo':[
  'demo/oels_demo.xml'
],
'qweb': [],
'summary': 'Academy managment',
'version': '1.0',
'application': True,
}
