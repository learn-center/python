class Demo:
    def __init__(self):
        print("inside __init__")


demo = Demo()
# demo.__init__() # not needed to invoke __init__, since its automatically called when instantiated as above


class Fruit:
    def __init__(self):
        print("1")


class Apple(Fruit):
    def __init__(self):
        # super()._init()
        print("2")

    def dummy():
        pass


obj = Apple()  # 2
# Apple defines its own constructor (_init), which overrides the __init_ of the parent class Fruit.
# The _init_ method of Fruit is not automatically called because Apple has its own _init_ that overrides it.
# If you wanted to also call the _init_ of Fruit, you would need to explicitly invoke it using super()._init() inside Apple's __init_, or remove __init_ in Apple class


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
