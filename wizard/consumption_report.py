from odoo import fields, models, tools, api,_
from odoo.exceptions import UserError

class ConsumptionReport(models.TransientModel):
    """ MRP Consumption wizard Report """
    _name = "mrp.consumption.wizard"
    _description = "MRP Consumption wizard Report"

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')
    manufacturing_order_id = fields.Many2many('mrp.production', string='Manufacturing Orders')
    summary = fields.Boolean('Summary')
    Date = fields.Date()
    Product = fields.Char()
    Order = fields.Char()
    Quantity = fields.Float()
    User = fields.Many2one('res.partner')
    Consumed = fields.Float()
    Remaining = fields.Float()
    Planned = fields.Float()

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['manufacturing_order_id', 'date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['manufacturing_order_id', 'date_from', 'date_to'])[0])
        return self.env['report'].get_action(self, 'mrp_account_report.report_consumption', data)

