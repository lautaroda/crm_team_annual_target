from odoo import fields, models, api

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    invoiced_target = fields.Float(string='Annual Invoicing Target')

    @api.depends('invoiced_target')
    def _compute_monthly_target(self):
        for team in self:
            team.monthly_target = team.invoiced_target / 12

    monthly_target = fields.Float(string='Monthly Target', compute='_compute_monthly_target', store=True)
    use_quotations = fields.Boolean(string="Use Quotations", default=False)
