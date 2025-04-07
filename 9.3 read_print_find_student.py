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


students = []
for i in range(0, 2):
    stud = Student()
    stud.read_student()
    students.append(stud)

for i in range(0, 2):
    students[i].print_student()

searchNo = input("Enter Serial No: ")
for i in range(0, len(students)):
    if students[i].sno == searchNo:
        print(
            f"Student with Serial No: {searchNo} found with Name: {students[i].sname} and Fee: {students[i].fee}"
        )
        break
    if i == len(students):
        print(f"Student with Serial No: {searchNo} is not found")
