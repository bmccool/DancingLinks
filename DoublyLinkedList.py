class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            self.insert_in_emptylist(data)
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            self.insert_in_emptylist(data)
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.start_node = new_node
                n.prev = new_node

    def traverse_list(self):
        retval = []
        if self.start_node is None:
            print("List has no element")
        else:
            n = self.start_node
            while n is not None:
                print(n.data , " ")
                retval.append(n.data)
                n = n.next
        return retval

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_at_end(self):
        # Check if the list is empty
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        # Handle case of one node in the list
        if self.start_node.next is None:
            self.start_node = None
            return
        # Handle all other cases
        n = self.start_node
        while n.next is not None:
            n = n.next
        # n is the last node, remove the refrence to it
        n.prev.next = None

    def delete_element_by_value(self, x):
        # Check if the list is empty
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        # Handle case of one node in the list
        if self.start_node.next is None:
            if self.start_node.data == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        # If the list is bigger than one node, and the first element matches...
        if self.start_node.data == x:
            self.start_node = self.start_node.next
            self.start_node.pref = None
            return

        # Traverse the list, stop if the node is found
        n = self.start_node
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
    
        if n.next is not None:
            # Note: if n.next is not none, it must be because the node was found
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            # n is the last node, check if it is the one to delete
            if n.data == x:
                n.prev.next = None
            else:
                print("Element not found")    

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list is empty, cannot reverse an empty list")
            return 
        p = self.start_node
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.start_node = p

class CircularDoublyLinkedList(DoublyLinkedList):
    """ 
    A circular doubly linked list is just a doubly linked list where we take
    care to make sure the 'last' node in the list points back to the head.
    A naive approach could be to check this condition after every operation
    i.e. the head.prev should point to the 'last' element, and there should be
    no empty pointers traversing the list in either direction.  This would be
    a pretty silly way to do it though, picking up an extra O(n) operation for
    things that don't need it.  
    """

