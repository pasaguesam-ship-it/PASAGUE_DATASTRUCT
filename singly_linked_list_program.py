class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, letter):
        new_node = Node(letter)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        print("Output:", end=" ")
        while current is not None:
            print(current.letter, end=" ")
            current = current.next
        print()


name_input = input("Enter your last name: ").upper()

linked_list = SinglyLinkedList()
for letter in name_input:
    linked_list.append(letter)

linked_list.display()
