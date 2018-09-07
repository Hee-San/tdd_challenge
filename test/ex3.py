import unittest
from io import StringIO
from ex3 import Address

class TestAddress(unittest.TestCase):
    def test_A1_validate_addr_spec(self):
        self.tests = {'@\n':'ok',
                'hoge@piyo.com\n':'ok',
                'hogehoge\n':'ng',
                'hoge@hoge@fuga\n':'ng'
                }

    def test_D1_validate_addr_spec(self):
        self.tests = {'@\n':'ok',
                'oge@piyo.com\n':'ok',
                'ogehoge\n':'ng',
                'oge@hoge@fuga\n':'ng'
                }

    def tearDown(self):
        for _in, _out in self.tests.items():
            _stdin = StringIO(_in)
            _stdout = StringIO()
            address = Address(_stdin, _stdout)
            address.validate_addr_spec()
            actual = _stdout.getvalue()
        
            self.assertEqual(actual, _out)

