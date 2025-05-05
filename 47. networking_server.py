import socket


server_socket_obj = socket.socket()
server_socket_obj.bind(("127.0.0.1", 8080))
server_socket_obj.listen(5)
print("Server started, waiting for the clients to connect..")

while True:
    client_socket_obj, addr = server_socket_obj.accept()
    print(f"Client connected successfully at {addr}.")

    while True:
        messge_from_client = client_socket_obj.recv(1024).decode("utf-8")
        print(messge_from_client)

        if messge_from_client.lower() == "exit":
            break

        client_socket_obj.send(bytes(f"{messge_from_client} from server", "utf-8"))

    client_socket_obj.close()
    break

server_socket_obj.close()
