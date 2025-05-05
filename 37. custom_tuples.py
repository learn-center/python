class MyTuple:
    def __init__(self, *args):
        self.Items = list(args)

    def __getitem__(self, ndx):
        return self.Items[ndx]

    def __eq__(self, value):
        if isinstance(value, MyTuple):
            for i in range(len(self.Items)):
                if value[i] != self.Items[i]:
                    return False
        else:
            return False

        return True


t1 = MyTuple(1, 2, 3)
t2 = MyTuple(10, 20, 30)
t3 = MyTuple(1, 2, 3)

print(t1[0])
print(t1[1])

if t1 == t2:
    print("t1 and t2 are equal")
else:
    print("t1 and t2 are not equal")

if t1 == t3:
    print("t1 and t3 are equal")
else:
    print("t1 and t3 are not equal")

if t1 == [1, 2, 3]:
    print("tuples are equal")
else:
    print("tuples are not equal")
