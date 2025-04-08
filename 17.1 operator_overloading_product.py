class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __eq__(self, prod):
        return (
            self.id == prod.id and self.name == prod.name and self.price == prod.price
        )

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"

    def __repr__(self):
        return f"{self.id} {self.name} {self.price}"


class ProductList:
    def __init__(self):
        self.products = []
        self.current = -1

    def __iadd__(self, prod: Product):
        self.products.append(prod)
        return self

    def __isub__(self, prod: Product):
        self.products.remove(prod)
        return self

    def __ge__(self, price: float):
        return [item for item in self.products if item.price >= price]

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.products):
            return self.products[self.current]
        else:
            raise StopIteration


p1 = Product(1001, "Laptop", 50000)
p2 = Product(1002, "Phone", 40000)
p3 = Product(1003, "Tablet", 10000)

plist = ProductList()

plist += p1
plist += p2
plist += p3

p6 = plist >= 35000
print(p6)  # using __repr__ dunder in Product class

for prod in p6:
    print(prod)  # using __str__ dunder in Product class

print(p1 == p3)
print(p1 == p1)

plist -= p2

for prod in plist:
    print(prod)
