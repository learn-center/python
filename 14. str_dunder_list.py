class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"


lst = []
lst.append(Product(1001, "Laptop", 50000))
lst.append(Product(1002, "Phone", 40000))

for item in lst:
    print(item)
