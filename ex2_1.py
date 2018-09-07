def my_round(value):
    return (value*2+1)//2

class Price:
    def calc_price(self, prices):
        if len(prices) == 0:
            return 0
        else:
            return my_round(sum(prices) * 1.1)

