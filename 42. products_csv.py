import csv


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"


product_list = list()
product_list.append(Product(1001, "Laptop", 50000))
product_list.append(Product(1002, "Phone", 40000))
product_list.append(Product(1003, "Tablet", 10000))

products_csv_file = open("products.csv", "w", newline="")
csvwriter = csv.writer(products_csv_file)
for product in product_list:
    csvwriter.writerow([product.id, product.name, product.price])
products_csv_file.close()

products_csv_file = open("products.csv", "r", newline="")
csvreader = csv.reader(products_csv_file)
for row in csvreader:
    print(row)
products_csv_file.close()
