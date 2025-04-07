x = int(input("enter a number"))
y = int(input("enter b number"))
z = int(input("enter c number"))

print(type(x))
print(x + y)
print("%d + %d = %d" % (x, y, x + y))
print(f"{x} + {y} = {x+y}")

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is smaller than {y}")

if x > y and y > z:
    print("a is greater than both b and c")
elif y > x and y > z:
    print("b is greater than both a and c")
else:
    print("c is greater than both a and b")

message = "a is greater than b" if x > y else "b is greater than a"
print(message)

if x > 35 and y > 35 and z > 35:
    if (x + y + z) / 3 > 60:
        print("a grade")
    elif (x + y + z) / 3 > 50:
        print("b grade")
    else:
        print("c grade")
else:
    print("fail")
