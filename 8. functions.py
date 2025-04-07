def sum(x: int, y: int) -> int:
    return x + y


result = sum(10, 20)
print(result)


def print_in_reverse(stringVal: str):
    print(stringVal[::-1])


# since print_in_reverse is not returning anything, print is printing None, take off print to just see reverse being printed
print(print_in_reverse("Hello"))
print_in_reverse("Hello")


def multiply_numbers(x: int, y: int):
    return x * y


print(multiply_numbers(10, 20))
print(multiply_numbers(y=30, x=20))  # named arguments


# multiple parameters can be passed into *args
def variable_args(*args):
    for arg in args:
        print(arg)


variable_args(
    [10, 20, 30, 40],
    (10, 20),
)


# key word arguments
def named_keyword_args(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


named_keyword_args(x=10, y=20, z="abc")
