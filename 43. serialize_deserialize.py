import json


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"


def converter(obj):
    if isinstance(obj, Product):
        return {"name": obj.name, "price": obj.price}


def to_product_obj(dict):
    return Product(**dict)


product = Product("Laptop", 50000)
print(product.__dict__)

product_json_str = json.dumps(product.__dict__)
print(product_json_str)

product_dict = json.loads(product_json_str)
print(product_dict)
print(Product(**product_dict))


product_json_str = json.dumps(product, default=converter)
print(product_json_str)

product_obj = json.loads(product_json_str, object_hook=to_product_obj)
print(product_obj)

fp = open("product.json", "w")
fp.write(product_json_str)
fp.close()

fp = open("product.json", "r")
product_json = fp.read()
print(product_json)
