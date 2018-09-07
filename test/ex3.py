import unittest
from io import StringIO
from ex3 import Address

class TestAddress(unittest.TestCase):
    def test_validate_addr_spec(self):
        A1_tests = {'@\n':'ok',
                    'hoge@piyo.com\n':'ok',
                    'hogehoge\n':'ng',
                    'hoge@hoge@fuga\n':'ng'
                    }

        for _in, _out in A1_tests.items():
            _stdin = StringIO(_in)
            _stdout = StringIO()
            address = Address(_stdin, _stdout)
            address.validate_addr_spec()
            actual = _stdout.getvalue()
        
            self.assertEqual(actual, _out)

