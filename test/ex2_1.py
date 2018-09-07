import unittest
from ex2_1 import Price

MILLION = 1000000

class TestPrice(unittest.TestCase):
    def test_calc_price(self):
        price = Price()
        self.assertEqual(price.calc_price([]), 0)
        self.assertEqual(price.calc_price([0]), 0)
        self.assertEqual(price.calc_price([1]), 1)
        self.assertEqual(price.calc_price([4]), 4)
        self.assertEqual(price.calc_price([5]), 6)
        self.assertEqual(price.calc_price([6]), 7)
        self.assertEqual(price.calc_price([10]), 11)
        self.assertEqual(price.calc_price([11]), 12)
        self.assertEqual(price.calc_price([15]), 17)
        self.assertEqual(price.calc_price([10,12]), 24)
        self.assertEqual(price.calc_price([40,16]), 62)
        self.assertEqual(price.calc_price([100,45]), 160)
        self.assertEqual(price.calc_price([50,50,55]), 171)
        self.assertEqual(price.calc_price([MILLION]), 1100000)
        self.assertEqual(price.calc_price([1000]), 1100)
        self.assertEqual(price.calc_price([20, 40]), 66)
        self.assertEqual(price.calc_price([30, 60, 90]), 198)
        self.assertEqual(price.calc_price([11, 12, 13]), 40)


        
