class List:
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append(item)

    def generator(self):
        count = 0
        while count < len(self.list):
            yield self.list[count]
            count += 1


lst = List()
lst.add(100)
lst.add(200)
lst.add(300)
lst.add(400)

for item in lst.generator():
    print(item)
