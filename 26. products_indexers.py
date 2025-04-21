class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} {self.price}"


class Collection:
    def __init__(self):
        self._products = []

    def add(self, item):
        self._products.append(item)

    def __getitem__(self, input):
        if isinstance(input, int):
            self.func = lambda product: product.id == input
        elif isinstance(input, str):
            self.func = lambda product: product.name == input
        else:
            self.func = input

        return [product for product in self._products if self.func(product)]


class List:
    def __init__(self):
        self._collection = Collection()

    @property
    def Items(self):
        return self._collection


productlist = List()
productlist.Items.add(Product(1001, "Laptop", 50000))
productlist.Items.add(Product(1002, "Phone", 40000))
productlist.Items.add(Product(1003, "Tablet", 10000))

product = productlist.Items[1002]
print(product)

product = productlist.Items["Laptop"]
print(product)

products = productlist.Items[lambda product: product.price <= 40000]
print(products)
