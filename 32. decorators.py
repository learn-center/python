def decorator(func):
    def wrapper(*args):
        print("Before the function call")
        result = func(*args)
        print("After the function call")
        return result

    return wrapper


# def sum(x, y):
#     return x + y

# wrapper = decorator(sum)
# print(wrapper)
# print(wrapper.__name__)
# print(wrapper(1, 2))


@decorator
def sum(x, y):
    return x + y


print(sum(1, 2))
