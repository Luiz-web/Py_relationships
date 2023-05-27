class Kart:
    def __init__(self):
        self.__products = []

    @property
    def products(self):
        return self.__products
    
    def list_products(self):
        for product in self.__products:
            print(f"{product.name} -> ${product.price}")
    
    def add_products(self, *itens):
        self.__products.extend(itens)

    def total(self):
        return f"TOTAL OF KART: {sum([item.price for item in self.__products])}"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

kart = Kart()
shirt, pants = Product("Shirt", 24.99), Product("Pants", 19.60)

kart.add_products(shirt, pants)
kart.list_products()
print(kart.total())