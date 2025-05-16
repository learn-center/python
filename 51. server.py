import socket
from threading import Thread


class ProcessMessage(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            for key, client in list(clients.items()):
                try:
                    client.settimeout(0.1)
                    message = client.recv(1024).decode("utf-8")
                    if message.lower() == "exit":
                        del clients[key]
                        client.close()
                    else:
                        to_client, msg = message.split(",", 1)
                        clients[int(to_client)].send(bytes(msg, "utf-8"))
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"Error : {e}")


server = socket.socket()
server.bind(("127.0.0.1", 8080))
server.listen(5)
clients = dict()
index = 1

process_message = ProcessMessage()
process_message.start()

print("Server started, waiting for the clients to connect..")
while True:
    try:
        client, addr = server.accept()
        clients[index] = client
        print(f"Client {index} connected from {addr}")
        index += 1
    except BlockingIOError:
        continue
