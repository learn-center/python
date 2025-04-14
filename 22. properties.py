class Product:
    def __init__(self):
        self._id = 0
        self._name = ""
        self._price = 0.0

    def set_Id(self, value):
        self._id = value

    def set_Name(self, value):
        self._name = value

    def set_Price(self, value):
        self._price = value

    def get_Id(self):
        return self._id

    def get_Name(self):
        return self._name

    def get_Price(self):
        return self._price

    Id = property(get_Id, set_Id)
    Name = property(get_Name, set_Name)
    Price = property(get_Price, set_Price)


product = Product()

# product.set_Id(1001)
# product.set_Name("Laptop")
# product.set_Price(450.0)
# print(f"{product.get_Id()} {product.get_Name()} {product.get_Price()}")

product.Id = 2001
product.Name = "iPad"
product.Price = 350.45
print(f"{product.Id} {product.Name} {product.Price}")
