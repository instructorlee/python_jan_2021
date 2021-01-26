# http://learn.codingdojo.com/m/108/5814/39773

class Store:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id): # 0, 1, 2, 3, 4 remove # 3 -> 0, 1, 2 , 4
        # self.products = self.products[:id] + self.products[id + 1]
        self.products.pop(id)

    def inflation(self, percent_increase):
        pass

    def set_clearance(self, category, percent_discount):
        pass

CLOTHING = 1
CANDY = 2

class Product:

    def __init__(self, name, price, category=CLOTHING):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        print (f"{self.name} - {self.price} / {self.category}")


store = Store('tg&y')
store.add_product(Product('shoes', 10))
store.add_product(Product('shirt', 9))
store.add_product(Product('bubble gum', 1, CANDY))
# print(store.products[0].name)
for product in store.products:
    product.print_info()