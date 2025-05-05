mydict1 = dict(one=1, two=2)
print(mydict1["one"])

mydict2 = {"One": 1, "Two": 2}
print(mydict2["One"])

print(mydict2.keys())

for key in iter(mydict2.keys()):
    print(f"key: {key}, value: {mydict2[key]}")

print(mydict2.values())

for value in iter(mydict2.values()):
    print(value)

if mydict2.get("hello") is None:
    print("Key not found")


class Student:
    def __init__(self, sno, marks):
        self.sno = sno
        self.marks = marks

    def __str__(self):
        return f"{self.sno} {self.marks}"


s1 = Student(1001, [10, 20, 30])

dct1 = {"1001": s1}
print(dct1["1001"])

s2 = Student(1002, [20, 30, 40])
s3 = Student(1003, [30, 40, 50])
dct2 = {"1001": (s2, s3)}
print(dct2["1001"])
