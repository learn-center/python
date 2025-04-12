list = [10, 20, 30, 40, 50]


def filter(condition):
    temp = []
    for val in list:
        if condition(val):
            temp.append(val)
    return temp


f_list = filter(lambda v: v < 30)
print(f_list)

f_list = filter(lambda v: v > 30)
print(f_list)


def expression(value):
    return value > 30


f_list = filter(expression)
print(f_list)
