class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


name_input = input("Enter your last name: ").upper()

stack = Stack()
for letter in name_input:
    stack.push(letter)

print("Output:", end=" ")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()
