class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.new_node: Node = None
        self.first_node: Node = None
        self.prev_node: Node = None

    def add(self, value):
        self.new_node = Node(value, None)

        if self.first_node is None:
            self.first_node = self.new_node

        if self.prev_node is not None:
            self.prev_node.next = self.new_node

        self.prev_node = self.new_node

    def show(self):
        while self.first_node is not None:
            print(self.first_node.data)
            self.first_node = self.first_node.next


l_list = LinkedList()
l_list.add(100)
l_list.add(200)
l_list.add(300)
l_list.add(400)

l_list.show()
