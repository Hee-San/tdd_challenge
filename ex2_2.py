import sys
from io import StringIO

def my_round(value):
    return int((value*2+1)//2)


class Price:
    def __init__(self, i, o):
        self._input = i
        self._output = o

    def calc_price(self):
        prices = list(map(int, (self._input.read().split(','))))
        ans = my_round(sum(prices) * 1.1)
        self._output.write(str(ans))
        return 0


if __name__ == '__main__': 
    price = Price(sys.stdin, sys.stdout)
    price.calc_price()
