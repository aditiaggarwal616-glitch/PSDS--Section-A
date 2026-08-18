#stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(self.top.data, "popped")
            self.top = self.top.next

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:")
s.display()

s.pop()

print("After pop:")
s.display()