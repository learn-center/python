def parent_decorator(func):
    def wrapper(*args):
        print("start parent_decorator")
        func(*args)
        print("end parent_decorator")

    return wrapper


def repeat(count):
    def child_decorator(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)

        return wrapper

    return child_decorator


@parent_decorator
@repeat(3)
def show(message):
    print(message)


show("Hello")
