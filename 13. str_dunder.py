class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print(self):
        print(f"{self.id} {self.name} {self.price}")

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"


prod = Product(1001, "Laptop", 50000)
prod.print()
print(prod)  # prod object will internally invoke __str__

x = 100
print(x)
# int class in python will override __str__ to return the value stored in the int variable
print(x.__str__())
