class Math:
    def __init__(self, data):
        self.data = data

    def sum(self, math):
        m = Math(0)
        m.data = self.data + math.data
        return m

    def print(self):
        print(self.data)

    def __str__(self):
        return str(self.data)


m1 = Math(100)
m2 = Math(200)
m3 = m1.sum(m2)
m3.print()
print(m3)
