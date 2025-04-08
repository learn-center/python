class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"


class Cart:
    def __init__(self):
        self.items = []
        self.current = -1

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        else:
            raise StopIteration


cart = Cart()
cart.add(Product(1001, "Laptop", 50000))
cart.add(Product(1002, "Phone", 40000))

for item in cart:
    print(item)
