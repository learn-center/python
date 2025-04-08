class Math2024:
    def sum(self, x, y):
        return x + y

    def subt(self, x, y):
        return x - y


class Math2025(Math2024):
    def mult(self, x, y):
        return x * y


m2024 = Math2024()
print(m2024.sum(40, 30))
print(m2024.subt(40, 30))

m2025 = Math2025()
print(m2025.sum(40, 30))
print(m2025.subt(40, 30))
print(m2025.mult(40, 30))
