from product_list import Products

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
