import unittest
import contextlib
from io import StringIO
from ex2_2 import Price


class TestPrice(unittest.TestCase):
    def test_calc_price(self):
        tests = {"10\n": "11\n",
                 "10,12\n": "24\n",
                 "10,12\n40,16\n": "24\n62\n",
                 "10,12\n\n40,16\n": "24\n0\n62\n",
                 "10,12\n\n40,16\n\n": "24\n0\n62\n0\n"
                }

        for _in, _out in tests.items():
            _input = StringIO(_in)  # これがスタブ
            _output = StringIO()  # これがスパイ
            price = Price(_input, _output)

            price.calc_price()
            actual = _output.getvalue()

            self.assertEqual(actual, _out)