class ParentOne:
    def print(self):
        print("ParentOne print")


class ParentTwo:
    def print(self):
        print("ParentTwo print")


class ChildOne(ParentOne, ParentTwo):
    pass


class ChildTwo(ParentTwo, ParentOne):
    pass


childTwo = ChildOne()
childTwo.print()

childTwo = ChildTwo()
childTwo.print()
