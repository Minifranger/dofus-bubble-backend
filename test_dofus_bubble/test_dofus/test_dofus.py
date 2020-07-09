import unittest

from dofus_bubble.dofus.lambdas import LambdasDofus


class TestDofus(unittest.TestCase):
    __DYNAMODB_TABLE__ = 'dofus-bubble'
    __event__ = {'body': None, 'pathParameters': None, 'queryStringParameters': None}
    __context__ = None

    def _test_response(self, result):
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('statusCode'), 200)
        [self.assertIsInstance(i, dict) for i in result.get('body')]
        self.assertEqual(result.get('body'), list({v['_id']: v for v in result.get('body')}.values()))

    def test_scan_weapons_by_price(self):
        result = LambdasDofus().scan_items_by_price(self.__event__, self.__context__, DYNAMODB_TABLE=self.__DYNAMODB_TABLE__)
        self._test_response(result)
