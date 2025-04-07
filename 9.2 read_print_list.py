class Student:
    sno: int
    sname: str
    fee: float

    def read_student(self):
        self.sno = input("Enter Serial No: ")
        self.sname = input("Enter Name: ")
        self.fee = input("Enter Fee: ")

    def print_student(self):
        print(f"{self.sno} {self.sname} {self.fee}")


studlist = []
for i in range(0, 5):
    stud = Student()
    stud.read_student()
    studlist.append(stud)

for i in range(0, 5):
    studlist[i].print_student()
