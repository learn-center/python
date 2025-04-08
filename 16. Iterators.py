class Bag:
    def __init__(self):
        self.items = []
        self.current = -1

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        print("invoked __iter__")
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        else:
            raise StopIteration


bag = Bag()
bag.add(1)
bag.add(2)
bag.add(3)
bag.add(4)

# for item in bag:
#     print(item)

itr = iter(bag)
for item in itr:
    print(item)

# print(next(itr))
