class Node:
    """
    Class to represent a single node in a linked list.
    """
    def __init__(self, value=0, next=None):
        self.value = value  # Value of the node
        self.next = next    # Reference to the next node


class SinglyLinkedList:
    """
    Class to represent the singly linked list.
    """
    def __init__(self):
        self.head = None  # Start of the list
        self.size = 0     # Number of nodes in the list

    def __str__(self):
        """
        String representation of the linked list.
        """
        if not self.head:
            return "Empty List"
        
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

    def is_empty(self):
        """
        Check if the linked list is empty.
        """
        return self.head is None

    def append(self, value):
        """
        Add a node at the end of the list.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, value):
        """
        Add a node at the beginning of the list.
        """
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1

    def insert(self, value, position):
        """
        Insert a node at a specific position (0-based index).
        """
        if position < 0 or position > self.size:
            raise IndexError("Index out of bounds.")
        
        if position == 0:
            self.prepend(value)
        elif position == self.size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(position - 1):  # Traverse to the node before the position
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def delete_by_value(self, value):
        """
        Delete the first node with the specified value.
        """
        if self.is_empty():
            print("List is empty, nothing to delete.")
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
        else:
            print(f"Value {value} not found in the list.")

    def delete_by_position(self, position):
        """
        Delete a node at a specific position (0-based index).
        """
        if position < 0 or position >= self.size:
            raise IndexError("Index out of bounds.")
        
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):  # Traverse to the node before the position
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def search(self, value):
        """
        Search for a value in the list and return its position (0-based index).
        """
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1  # Value not found

    def reverse(self):
        """
        Reverse the linked list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Example Usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
print("Original List:", sll)  # Output: 10 -> 20 -> 30

sll.prepend(5)
print("After Prepending 5:", sll)  # Output: 5 -> 10 -> 20 -> 30

sll.insert(15, 2)
print("After Inserting 15 at position 2:", sll)  # Output: 5 -> 10 -> 15 -> 20 -> 30

sll.delete_by_value(20)
print("After Deleting value 20:", sll)  # Output: 5 -> 10 -> 15 -> 30

sll.delete_by_position(0)
print("After Deleting position 0:", sll)  # Output: 10 -> 15 -> 30

print("Search for value 15:", sll.search(15))  # Output: 1
print("Search for value 50:", sll.search(50))  # Output: -1

sll.reverse()
print("Reversed List:", sll)  # Output: 30 -> 15 -> 10
