def add_str_repr(cls):
    def custom_str(self):
        return f"{cls.__name__}"

    def custom_repr(self):
        return f"{cls.__name__} {self.__dict__}"

    cls.__str__ = custom_str
    cls.__repr__ = custom_repr

    return cls


@add_str_repr
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 5000)
print(product)

print(str(product))
print(product.__str__())

print(repr(product))
print(product.__repr__())
