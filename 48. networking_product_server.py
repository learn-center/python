import socket
import json

server_socket_obj = socket.socket()
server_socket_obj.bind(("127.0.0.1", 8080))
server_socket_obj.listen(5)
print("Server started, waiting for the clients to connect..")

while True:
    client_socket_obj, addr = server_socket_obj.accept()
    print(f"Client connected successfully at {addr}.")

    while True:
        json_str = client_socket_obj.recv(1024).decode("utf-8")
        if json_str.lower() == "exit":
            break
        else:
            product_dict = json.loads(json_str)
            print(product_dict)

    client_socket_obj.close()
    break

server_socket_obj.close()
