from odoo import fields, models, api

class WorkOnWeb(models.Model):
    _name='workon.web'
    _description ='Controller Works'


    name = fields.Char('Name')
    std_class=fields.Char('Class')

