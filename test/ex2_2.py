import unittest
import contextlib
from io import StringIO
from ex2_2 import Price

class TestPrice(unittest.TestCase):
    def test_calc_price(self):
        _input = StringIO(str(10))  # これがスタブ
        _output = StringIO()  # これがスパイ
        price = Price(_input, _output)

        price.calc_price()
        actual = _output.getvalue()

        self.assertEqual(actual, str(11))

        _input = StringIO("10,12")  # これがスタブ
        _output = StringIO()  # これがスパイ
        price = Price(_input, _output)

        price.calc_price()
        actual = _output.getvalue()

        self.assertEqual(actual, str(24))

