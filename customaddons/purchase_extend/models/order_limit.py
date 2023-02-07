from odoo import models, fields


class OrderLimit(models.Model):
    _name = 'order.limit'
    employee_order_limit = fields.Many2many('employee.order.limit', string="Employee order limit")