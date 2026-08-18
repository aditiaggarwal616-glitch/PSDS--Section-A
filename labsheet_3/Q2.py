#queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "enqueued")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data, "dequeued")
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

q.dequeue()

print("After dequeue:")
q.display()