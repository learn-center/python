t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

print(t1[1])
print(t1 == t2)
print(t1[0:3])


t3 = tuple((100, 200, (1, 2, 3), [10, 20, 30], ("hi", "hello")))
print(t3[0])
print(t3[4])
print(t3[4][1])


for item in t3:
    if isinstance(item, tuple) or isinstance(item, list):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)

# can change the value in a list
print(t3[3][0])
t3[3][0] = "changed"
print(t3[3][0])

# can not change the value in a tuple
# t3[0] = "changed"  # TypeError: 'tuple' object does not support item assignment

# newlist = ["one", "two"]
# t3[3] = newlist  # TypeError: 'tuple' object does not support item assignment
