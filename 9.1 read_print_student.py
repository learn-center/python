class Student:
    id: int
    name: str
    fee: float

    def read_student(self):
        self.id = input("Enter Serial No: ")
        self.name = input("Enter Name: ")
        self.fee = input("Enter Fee: ")

    def print_student(self):
        print(f"{self.id} {self.name} {self.fee}")


stud = Student()
stud.read_student()
stud.print_student()
