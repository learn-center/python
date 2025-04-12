class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} {self.price}"


class ProductList:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def filter(self, condition):
        temp = []
        for product in self.products:
            if condition(product):
                temp.append(product)
        return temp

    def filter_v2(self, condition):
        return [product for product in self.products if condition(product)]


plist = ProductList()
plist.add(Product(1001, "Laptop", 50000))
plist.add(Product(1002, "Phone", 40000))
plist.add(Product(1003, "Tablet", 10000))


def expression(product: Product):
    return product.price > 30000


# f_plist = plist.filter(expression)
# f_plist = plist.filter(lambda product: product.price > 30000)
f_plist = plist.filter(lambda product: product.name != "Phone")
f_plist = plist.filter_v2(lambda product: product.price <= 40000)

print(f_plist)
