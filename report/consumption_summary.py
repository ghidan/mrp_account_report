import time
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError



class ConsumptionSummaryReport(models.AbstractModel):
    _name = 'report.mrp_account_report.report_consumption'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        product_records = []
        orders = self.env['stock.move'].search([('raw_material_production_id', 'in', docs.manufacturing_order_id)])
        if docs.date_from and docs.date_to:
            for order in orders:
                if parse(docs.date_from) <= parse(order.date) and parse(docs.date_to) >= parse(order.date):
                    product_records.append(order);
        else:
            raise UserError("Please enter duration")

        docargs = {
            'doc_ids': self.ids,
            'doc_model': 'report.mrp_account_report.report_consumption',
            'docs': docs,
            'time': time,
            'orders': product_records
        }
        return self.env['report'].render('mrp_account_report.report_consumption', docargs)