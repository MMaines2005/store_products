
class Products:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        result = self.final_price - self.stock_price
        return result

class bread(Products):
    def __init__(self, name, stock_price, final_price):
        super().__init__(name, stock_price, final_price)

class fruit(Products):
    def __init__(self, name, stock_price, final_price):
        super().__init__(name, stock_price, final_price)
    
    def print_info(self):
        print(self)

