add = lambda x, y: x + y
print(add(100, 200))

subt = lambda x, y: x - y
print(subt(300, 200))


def calc(x, y, operation):
    return operation(x, y)


value = calc(10, 20, lambda x, y: x + y)
print(value)


def calculator(operation):
    if operation == "+":
        return lambda x, y: x + y
    elif operation == "-":
        return lambda x, y: x - y
    elif operation == "*":
        return lambda x, y: x * y


value = calculator("+")
print(value(10, 20))
print(calculator("-")(20, 10))
print(calculator("*")(20, 10))


def fullname(firstname):
    return lambda lastname: f"{firstname} {lastname}"


print(fullname("John")("Wright"))
