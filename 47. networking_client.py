import socket


client_socket_obj = socket.socket()
client_socket_obj.connect(("127.0.0.1", 8080))
print("Connected to server successfully..")

while True:
    message_to_server = input("enter message to server: ")
    client_socket_obj.send(bytes(message_to_server, "utf-8"))

    if message_to_server.lower() == "exit":
        break

    while True:
        message_from_server = client_socket_obj.recv(1024).decode("utf-8")
        print(f"Server reply: {message_from_server}")
        break

client_socket_obj.close()
