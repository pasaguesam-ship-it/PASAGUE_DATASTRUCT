from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0


name_input = input("Enter your last name: ").upper()

queue = Queue()
for letter in name_input:
    queue.enqueue(letter)

print("Output:", end=" ")
while not queue.is_empty():
    print(queue.dequeue(), end=" ")
print()
