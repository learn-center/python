class List:
    store = []

    def __init__(self, *args):
        for value in args:
            self.add(value)

    def add(self, value):
        self.store.append(value)

    def find(self, value) -> int:
        for i in range(0, len(self.store)):
            if self.store[i] == value:
                return i + 1
        return -1

    def print(self):
        print(" ".join([str(i) for i in self.store]))


lst = List(10, 20, 30, 40)

lst.add(50)
lst.add(60)
lst.add(70)

val = 20
position = lst.find(val)
print(f"Position of {val} : {position}")

lst.print()
