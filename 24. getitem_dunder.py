class Car:
    def __init__(self):
        self._brands = []

    @property
    def Brands(self):
        return self._brands

    def __getitem__(self, ndx):
        return self._brands[ndx]


car = Car()
car.Brands.append("Benz")
car.Brands.append("Toyota")
car.Brands.append("Honda")
car.Brands.append("Skoda")

print(car.Brands)
print(car[0])
print(car[1])
