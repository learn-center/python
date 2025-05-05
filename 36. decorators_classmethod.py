class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.count += 1
        # Employee.count += 1

    @classmethod
    def change_count(cls, value):
        cls.count = value

    def __repr__(self):
        return f"name: {self.name} salary: {self.salary} self.count: {self.count} Employee.count: {Employee.count}"


e1 = Employee("abc", 5000)
print(e1)

e2 = Employee("cde", 4000)
print(e2)

e3 = Employee("fgh", 6000)
print(e3)


Employee.change_count(100)
print(e1)
print(e2)
print(e3)
