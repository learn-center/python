import threading
import csv
import time
from queue import Queue


class Product:
    def __init__(self, id: int, name: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.quantity}"


def produce(condition, q):
    with condition, open("product_producer.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if q.full():
                condition.notify()
                condition.wait()

            product = Product(int(row[0]), row[1], float(row[2]), int(row[3]))
            q.put(product)
            print(f"Produced: {product}")


def consume(condition, q):
    with condition:
        while q.full():
            with open(f"{time.time()}.csv", "w", newline="") as file:
                csv_writer = csv.writer(file)
                while not q.empty():
                    product = q.get()
                    print(f"Consumed: {product}")
                    csv_writer.writerow(
                        [
                            product.id,
                            product.name,
                            product.price,
                            product.quantity,
                            (product.price * product.quantity),
                            time.time(),
                        ]
                    )

            if q.empty():
                condition.notify()
                condition.wait()


queue = Queue(maxsize=5)
condition = threading.Condition()
t_producer = threading.Thread(target=produce, args=(condition, queue))
t_consumer = threading.Thread(target=consume, args=(condition, queue))

t_producer.start()
t_consumer.start()

t_producer.join()
t_consumer.join()

print("Completed")
