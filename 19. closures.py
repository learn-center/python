def calculate(x, y, action):
    return action(x, y)


def add(x, y):
    return x + y


def subt(x, y):
    return x - y


value = calculate(10, 20, add)
print(value)

value = calculate(1000, 200, subt)
print(value)
