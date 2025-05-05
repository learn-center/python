import pickle


class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: Id: {self.id}, Name: {self.name}, Price: {self.price}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self):
        id = int(input("Enter Id: "))
        name = input("Enter Name: ")
        price = float(input("Enter Price: "))

        self.products.append(Product(id, name, price))
        self.save()

    def find_in_cart(self):
        id = int(input("Enter an Id to find: "))
        with open("cart.pickle", "rb") as fp:
            while True:
                try:
                    product = pickle.load(fp)
                    if product.id == id:
                        print(f"Product found with Id: {id}. {product}")
                        break
                except EOFError:
                    print(f"Product not found with Id: {id}.")
                    break

    def save(self):
        with open("cart.pickle", "wb") as file:
            for product in self.products:
                pickle.dump(product, file)


cart = Cart()
print("\nPlease choose from the following:")
while True:
    ip = input("Type add/find/exit: ")
    if ip == "add":
        cart.add_product()
    elif ip == "find":
        cart.find_in_cart()
    elif ip == "exit":
        cart.save()
        break
