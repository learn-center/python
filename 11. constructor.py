class Demo:
    def __init__(self):
        print("inside __init__")


demo = Demo()
# demo.__init__() # not needed to invoke __init__, since its automatically called when instantiated as above


class Student:
    # number: int
    # name: str
    # fee: float

    # variables in the constructors will be automatically made available at class level, so no declaration is required
    def __init__(self, num, name, fee):
        self.number = num
        self.name = name
        self.fee = fee

    def print_student(self):
        print(f"{self.number} {self.name} {self.fee}")


stud = Student(1001, "Rick", 4500)
stud.print_student()
