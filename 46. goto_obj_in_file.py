import pickle


class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: Id: {self.id}, Name: {self.name}, Price: {self.price}"


products = [
    Product(1001, "lenovo", 5000),
    Product(1002, "dell", 3000),
    Product(1003, "acer", 6000),
]

with open("sequence.pickle", "wb") as file:
    pid_positions = dict()
    for product in products:
        pid_positions[product.id] = file.tell()
        pickle.dump(product, file)

pid = int(input("Enter pid to find:"))
products_deserialized = []
with open("sequence.pickle", "rb") as file:
    file.seek(pid_positions[pid])
    products_deserialized.append(pickle.load(file))

for p in products_deserialized:
    print(p)
