class Queue:
    def __init__(self):
        self.data = list()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        del self.data[0]

    def iterator(self):
        return self.data


queue = Queue()
queue.enqueue(100)
queue.dequeue()
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
queue.dequeue()
queue.dequeue()

for item in queue.iterator():
    print(item)
