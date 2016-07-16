from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']


class Sale:
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta

    quotation_date = fields.Date('Quotation Date', states={
           'reaonly' : ~Eval('state').in_(['draft', 'quotation']),
           }, depends=['state'])
