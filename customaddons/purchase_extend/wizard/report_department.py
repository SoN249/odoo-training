from odoo import fields, models, api, _


class ReportDepartment(models.TransientModel):
    _name = 'report.department'
    _description = 'Report Department Wizard'

    month = fields.Selection([
        ('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'),
        ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'),
        ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')
    ], string='Month', required=True)
    department_id = fields.Many2many('hr.department', string='Department')

    # Filter data by month and department name
    def btn_confirm(self):
        department_name = self.department_id.mapped('name')

        if self.month and self.department_id:
            context = {
                'name': _("Report Department"),
                'view_mode': 'tree',
                'res_model': 'hr.department',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('hr.view_department_tree').id,
                'target': 'current',
                'domain': [('create_month', '=', self.month), ('name', 'in', department_name)],
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        else:
            context = {
                'name': _("Report Department"),
                'view_mode': 'tree',
                'res_model': 'hr.department',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('hr.view_department_tree').id,
                'target': 'current',
                'context': {'create': False, 'edit': False, 'delete': False},
                'domain': [('create_month', '=', self.month)]
            }
        return context