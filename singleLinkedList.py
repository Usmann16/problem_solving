class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_last_occurrence(self, value):
        current = self.head
        last_occurrence_node = None
        
        # Traverse the linked list to find the last occurrence
        while current:
            if current.data == value:
                last_occurrence_node = current
                # Store the previous node only when we find a matching value
                # This will ensure it points to the last occurrence's previous node
                
            current = current.next

        # If no occurrence was found
        if not last_occurrence_node:
            return
        
        # If the last occurrence is the head node
        if last_occurrence_node == self.head:
            self.head = self.head.next
        else:
            # Remove the last occurrence
            current = self.head
            while current and current.next != last_occurrence_node:
                current = current.next
            if current:
                current.next = last_occurrence_node.next

    def reverse_linked_list(self):
        if self.head is None:
            return
        current = self.head
        new_list = LinkedList()

        while current:
            new_node = Node(current.data)
            # new_node.data = current.data
            if new_list is None:
                new_list = new_node
            else:
                new_node.next = new_list.head
                new_list.head = new_node
            current = current.next
        
        self.head = new_list.head

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(4)
    # ll.append(2)

    print("Original Linked List:")
    ll.print_list()

    # ll.remove_last_occurrence(0)
    ll.reverse_linked_list()
    ll.print_list()
    # print("Linked List after removing last occurrence of 2:")
    # ll.print_list()
