def generator():
    yield 1
    yield 2
    yield 3


gen = generator()
print(gen)

print(next(gen))
print(gen.__next__())


new_gen = generator()
for item in new_gen:
    print(item)


def my_range(start, end):
    count = start
    while count < end:
        yield count
        count += 1


for item in my_range(10, 15):
    print(item)
