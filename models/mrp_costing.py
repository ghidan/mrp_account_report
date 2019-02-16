from odoo import models, fields, api ,_
from odoo.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.tools import float_compare


class MrpCosting(models.Model):
    _name = "mrp.costing"
    _description = "MRP Costing Model"
    _rec_name = "product_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product_id = fields.Many2one('product.product',
                              string='Product', domain=[('type', 'in', ['product', 'consu'])], required=True)
    order_id = fields.Many2one('mrp.production', string='Order')
    user_id = fields.Many2one('res.users', string='User')
    cost = fields.Float(string='Cost', related='product_id.standard_price')
    date = fields.Datetime(string='Date')


class MrpProduction_inherit(models.Model):
    _inherit = 'mrp.production'

    @api.multi
    def button_mark_done(self):
        self.env['mrp.costing'].create({
            'product_id': self.product_id.id,
            'order_id': self.id,
            'user_id': self.user_id.id,
            'date': fields.Datetime.now(), })
        return super(MrpProduction_inherit, self).button_mark_done()