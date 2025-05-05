import pickle


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"


def read_pickled_objects():
    with open("products-check.pickle", "rb") as file:
        while True:
            try:
                product = pickle.load(file)
                print(type(product))
                yield product
            except EOFError:
                break


p1 = Product("HP", 4500)
p2 = Product("DELL", 4500)
p3 = Product("LENOVO", 4500)
data = [p1, p2, p3]
with open("products-check.pickle", "wb") as file:
    for item in data:
        pickle.dump(item, file)

for product in read_pickled_objects():
    print(product)
