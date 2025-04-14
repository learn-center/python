class Product:
    def __init__(self):
        self._id = 0
        self._name = ""
        self._price = 0.0

    @property
    def Id(self):
        return self._id

    @Id.setter
    def Id(self, value):
        if not isinstance(value, int):
            raise "Value should be an integer"
        if value < 100:
            raise "Value should start from 101"
        self._id = value

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Price(self):
        return self._price

    @Price.setter
    def Price(self, value):
        self._price = value

    @Price.deleter
    def Price(self):
        del self._price


product = Product()
product.Id = 1001
product.Name = "Laptop"
product.Price = 4500.50

print(f"{product.Id} {product.Name} {product.Price}")
del product.Price
# print(f"{product.Id} {product.Name} {product.Price}") #error: 'Product' object has no attribute '_price'.
