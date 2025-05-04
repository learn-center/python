class Stack:
    def __init__(self):
        self.data = list()
        self.current_ndx = 0

    def push(self, value):
        self.data.insert(self.current_ndx, value)
        self.current_ndx += 1

    def pop(self):
        self.current_ndx -= 1

    # def pop(self):
    #     self.current_ndx -= 1
    #     del self.data[self.current_ndx]

    def iterator(self):
        return self.data[0 : self.current_ndx][::-1]


stack = Stack()
stack.push(100)
stack.push(200)
stack.pop()
stack.pop()
stack.push(300)
stack.push(400)
stack.pop()
stack.pop()
stack.push(500)
stack.push(700)
stack.push(800)
stack.pop()
stack.push(600)

for item in stack.iterator():
    print(item)
