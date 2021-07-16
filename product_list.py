
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

class Store:

    product = {}

    def __init__(self, name):
        self.name = name
        Store.product = {}

    def load_item(self, product, count):
        if product not in self.product:
            self.product[product] = count
        else:
            self.product[product] += count

    def list_products(self, product_class=object):
        for product in self.product:
            if isinstance(product, product_class):
                print(f"{self.name} - {self.product[product]} counts")

    def sell_item(self, product):
        if product in self.product and self.product[product] > 0:
            return True

    def total_income(self):

        total_stock_price = 0
        total_final_price = 0
        for product in self.product:
            total_stock_price += self.product[product] * product.stock_price
            total_final_price += self.product[product] * product.final_price
        income = total_final_price - total_stock_price
        return income


fru1 = fruit("Apple", 1, 5)
fru2 = fruit("Mango", 5, 10)
bread1 = bread("Banana Nut", 3, 7)
bread2 = bread("BlueBerry Bread", 1, 5)

store = Store("Market")

#load products

store.load_item(fru1, 1)
store.load_item(fru2, 0)
store.load_item(bread1, 2)
store.load_item(bread2, 1)

#checks/ prints/functions

store.list_products(bread)
print(store.sell_item(bread1))
print(store.total_income())
store.load_item(fru2, 1)
store.list_products()
print(store.total_income())
