class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, letter):
        new_node = Node(letter)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def display_forward(self):
        current = self.head
        print("Output (forward):", end=" ")
        while current is not None:
            print(current.letter, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        print("Output (backward):", end=" ")
        while current is not None:
            print(current.letter, end=" ")
            current = current.prev
        print()


name_input = input("Enter your last name: ").upper()

dll = DoublyLinkedList()
for letter in name_input:
    dll.append(letter)

dll.display_forward()
dll.display_backward()
