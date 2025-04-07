class Math:
    def add(self):
        return 10 + 20

    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c


math = Math()

# This will raise an error because the last method is the only one that will be used
# print(math.add())

# This will raise an error because the last method is the only one that will be used
print(math.add(1, 2))

print(math.add(1, 2, 3))  # This will work

print(math.add(1, 2, c=3))  # This will work

# The last method will be used, and the previous ones will be ignored.
