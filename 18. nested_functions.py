def outer():
    x = 100

    def inner():
        print(x)

    inner()


outer()


def calculate(x, y):
    def sum():
        return x + y

    return sum


calc = calculate(10, 20)
print(calc())
