import socket
import json


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} {self.price}"


client_socket_obj = socket.socket()
client_socket_obj.connect(("127.0.0.1", 8080))
print("Connected to server successfully..")

while True:
    ip = input("Do you want to send a product to server? (y/n): ")
    if ip == "y":
        name = input("Enter product name: ")
        price = float(input("Enter Price: "))
        product = Product(name, price)
        client_socket_obj.send(bytes(json.dumps(product.__dict__), "utf-8"))
    elif ip == "n":
        client_socket_obj.send(bytes("exit", "utf-8"))
        break

client_socket_obj.close()
