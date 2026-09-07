# Infix to Postfix Conversion using Stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1] if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0
def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""

    for char in expression:
        if char.isalnum():
            postfix += char

        elif char == '(':
            stack.push(char)

        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(char)):
                postfix += stack.pop()

            stack.push(char)

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


expression = input("Enter infix expression: ")
print("Postfix expression:", infix_to_postfix(expression))