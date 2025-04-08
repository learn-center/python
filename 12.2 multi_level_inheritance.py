class Math2024:
    def __init__(self):
        print("Math2024 __init__")

    def sum(self, x, y):
        return x + y


class Math2025(Math2024):
    def __init__(self):
        print("Math2025 __init__")

    def subt(self, x, y):
        print("inside 2025 subt")
        return x - y


class Math2026(Math2025):
    def __init__(self):
        print("Math2026 __init__")

    def mult(self, x, y):
        return x * y

    def subt(self, x, y):
        print("inside 2026 subt")
        return super().subt(x, y)


m2026 = Math2026()
# print(m2026.sum(40, 30))
# print(m2026.subt(40, 30))
# print(m2026.mult(40, 30))
