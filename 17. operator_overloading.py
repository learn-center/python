class Math:
    def __init__(self, value):
        self.data = value

    def sum(self, math):
        m = Math(0)
        m.data = self.data + math.data
        return m

    # overriding __add__ dunder which overrides + operator
    def __add__(self, math):
        m = Math(0)
        m.data = self.data + math.data
        return m

    def __sub__(self, math):
        m = Math(0)
        m.data = self.data - math.data
        return m

    def __le__(self, math):
        return self.data <= math.data

    def __str__(self):
        return str(self.data)


m1 = Math(100)
m2 = Math(200)
m3 = m1.sum(m2)
print(m3)

m4 = m1 + m2  # operator overloading
print(m4)

m5 = m2 - m1
print(m5)

print(m2 <= m1)
