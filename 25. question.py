class Car:
    def __init__(self):
        self._brands = []

    def add(self, item):
        self._brands.append(item)

    def __getitem__(self, ndx):
        return self._brands[ndx]


class List:
    def __init__(self):
        self._car = Car()

    @property
    def Items(self):
        return self._car

    # def __getitem__(self, ndx):
    #     return self.Items[ndx]


list = List()
list.Items.add("Benz")
list.Items.add("Toyota")
list.Items.add("Honda")
list.Items.add("Skoda")

print(list.Items[0])
print(list.Items[1])

# print(list[0])
# print(list[1])
