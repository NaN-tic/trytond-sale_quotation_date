# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleQuotationDateTestCase(ModuleTestCase):
    'Test Sale Quotation Date module'
    module = 'sale_quotation_date'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            SaleQuotationDateTestCase))
    return suite
