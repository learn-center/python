import pickle


class Catagory:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Product:
    def __init__(self, name: str, price: float, category: Catagory):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"


category = Catagory("Electronics")
p1 = Product("HP", 4500, category)
p2 = Product("DELL", 4500, category)
p3 = Product("LENOVO", 4500, category)

# with open("products.pickle", "wb") as fp:
#     pickle.dump(p1, fp)
#     pickle.dump(p2, fp)
#     pickle.dump(p3, fp)

# with open("products.pickle", "rb") as fp:
#     p11 = pickle.load(fp)
#     p12 = pickle.load(fp)
#     p13 = pickle.load(fp)

# print(p11)
# print(p12)
# print(p13)

products = [p1, p2, p3]
with open("products.pickle", "wb") as fp:
    pickle.dump(products, fp)

with open("products.pickle", "rb") as fp:
    while True:
        try:
            temp = pickle.load(fp)
            # products.append(temp)
        except EOFError:
            break

for p in products:
    print(p)


product_lst = []
product_lst.append({"name": "Laptop", "price": 4500})
product_lst.append({"name": "Computer", "price": 6500})
product_lst.append({"name": "Mobile", "price": 9500})

with open("products_lst.pickle", "wb") as file:
    pickle.dump(product_lst, file)

with open("products_lst.pickle", "rb") as file:
    product_lst_temp = pickle.load(file)

for p in product_lst_temp:
    print(p)
