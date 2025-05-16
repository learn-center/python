import socket
from threading import Thread


class ProcessMessage(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client

    def run(self):
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8").strip()
                if not message or message == "exit":
                    print("Disconnected from server.")
                    break
                else:
                    print(f"Anonymous: {message}")
            except Exception as e:
                print("Error:", e)
                break


client = socket.socket()
client.connect(("127.0.0.1", 8080))

process_message = ProcessMessage(client)
process_message.start()

while True:
    message = input("Enter message (to_client,message or 'exit' to quit): ").strip()
    client.send(bytes(message, "utf-8"))

    if message.lower() == "exit":
        break
