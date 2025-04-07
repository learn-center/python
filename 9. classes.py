class Student:
    id: int
    name: str
    fee: float


stud = Student()
stud.id = 1001
stud.name = "John"
stud.fee = 4500.58

print(f"{stud.id} {stud.name} {stud.fee}")
print(type(stud))
