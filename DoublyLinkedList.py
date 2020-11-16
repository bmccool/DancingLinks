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

    def delete_at_end(self, delimiter=None):
        # Check if the list is empty
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        # Handle case of one node in the list
        if self.start_node.next == delimiter:
            self.start_node = None
            return
        # Handle all other cases
        n = self.start_node
        while n.next != delimiter:
            n = n.next
        # n is the last node, remove the refrence to it
        n.prev.next = None

    def delete_element_by_value(self, x, delimiter=None):
        # Check if the list is empty
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        # Handle case of one node in the list
        if self.start_node.next == delimiter:
            if self.start_node.data == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        # If the list is bigger than one node, and the first element matches...
        if self.start_node.data == x:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return

        # Traverse the list, stop if the node is found
        n = self.start_node
        while n.next != delimiter:
            if n.data == x:
                break
            n = n.next
    
        if n.next != delimiter:
            # Note: if n.next is not the delimiter, it must be because the node was found
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            # n is the last node, check if it is the one to delete
            if n.data == x:
                n.prev.next = None
            else:
                print("Element not found")    

    def reverse_linked_list(self, delimiter=None):
        if self.start_node is None:
            print("The list is empty, cannot reverse an empty list")
            return 
        p = self.start_node
        q = p.next
        p.next = None
        p.prev = q
        while q != delimiter:
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
    def insert_in_emptylist(self, data):
        super().insert_in_emptylist(data)
        self.start_node.next = self.start_node
        self.start_node.prev = self.start_node

    def insert_at_start(self, data):
        if self.start_node == None:
            self.insert_in_emptylist(data)
        else:
            last_node = self.start_node.prev
            super().insert_at_start(data)
            self.start_node.prev = last_node
            last_node.next = self.start_node         

    def insert_at_end(self, data):
        """ Doubly linked list relies on tail.next being null to find the end
        This won't work if the list is circular so this needs to be written from scratch"""
        if self.start_node is None:
            self.insert_in_emptylist(data)
            return
        n = self.start_node
        while n.next != self.start_node:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        new_node.next = self.start_node
        self.start_node.prev = new_node

    def insert_after_item(self, x, data):
        super().insert_after_item(x, data)
        #Scenarios:
        #1: We didn't insert anything, head and tail didn't change
        #2: We inserted in the middle, head and tail didn't change
        #3: We inserted after the first item, head and tail didn't change (more than 1 item in the list)
        #4: We inserted after the last item, tail changed to the new item (this covers #3 with only 1 item)
        # So we really only need to check for scenario 4
        if self.start_node.prev.next == self.start_node:
            # If the current tail still points to the head, do nothing
            pass
        else:
            new_tail = self.start_node.prev.next.next
            # We have inserted after the old tail,
            # Update the new tail to point back to the head
            new_tail.next = self.start_node
            #Update the head to point to the new tail
            self.start_node.prev = new_tail

    def insert_before_item(self, x, data):
        """ Insert before makes use of None to check for the end of the list
        So this will need to be rewritten for the circular doubly linked list"""
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n.next != self.start_node:
                if n.data == x:
                    break
                n = n.next
            if n.data != x:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev

                # If we are inserting at the begining...
                if n == self.start_node:
                    # Set the new start node...
                    self.start_node = new_node
                    # And set the tail to the new start node
                    new_node.prev.next = self.start_node
                else:
                    n.prev.next = new_node
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
                if n.next == self.start_node:
                    # We have reached the end of the list
                    break
                n = n.next
        return retval

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.next == self.start_node:
            self.start_node = None
            return
        tail = self.start_node.prev
        self.start_node = self.start_node.next
        self.start_node.prev = tail

    def delete_at_end(self):
        # Need to update the head and tail IFF there is more than 1 node
        if self.start_node != None:
            if self.start_node.next != self.start_node:
                new_tail = self.start_node.prev.prev
                super().delete_at_end(delimiter=self.start_node)
                self.start_node.prev = new_tail
                new_tail.next = self.start_node
                return
        # Other cases are handled by super
        super().delete_at_end(delimiter=self.start_node)
        return

    def delete_element_by_value(self, x):
        if self.start_node != None:
            old_tail = self.start_node.prev
            old_head = self.start_node
        super().delete_element_by_value(x, delimiter=self.start_node)
        # If the list is not empty...
        if self.start_node != None:
            # If there is only one element left
            if self.start_node.next == None:
                self.start_node.next = self.start_node
                self.start_node.prev = self.start_node
            # If the head stayed the same...
            elif self.start_node == old_head:
                # Check if the tail was deleted
                if self.start_node.prev.prev.next == None:
                    # Tail was deleted, fix the pointers
                    self.start_node.prev.prev.next = self.start_node
                    self.start_node.prev = self.start_node.prev.prev
            # If the head was changed...
            elif self.start_node != old_head:
                # Head was deleted, fix the pointers
                self.start_node.prev = old_tail
                old_tail.next = self.start_node

    def reverse_linked_list(self):
        if self.start_node != None:
            old_tail = self.start_node.prev
            old_head = self.start_node
            super().reverse_linked_list(delimiter=self.start_node)
            # old tail is new head, link it to the new tail (old head)
            old_tail.prev = old_head
            # old head is new tail, link it to the new head (old tail)
            old_head.next = old_tail
        # implicit else, an empty list is already reversed?

class DataObject:
    def __init__(self):
        self.L = None # Left
        self.R = None # Right
        self.U = None # Up
        self.D = None # Down
        self.C = None # The C field of each object points to the column object at the head of the relevant column.

class ColumnHeader(DataObject):
    def __init__(self):
        # ColumnHeaders contain all the fields of a DataObject...
        super().__init__()
        # And two additional fields
        self.S = None #Size, Number of 1s in this column
        self.N = None #Name, symbolic identifies for printing answers

class ColumnObject():
    #Contains All List Headers
    #TODO This class seems misnamed, its more meta than just columns
    def __init__(self):
        self.root = ColumnHeader() # aka 'h', only uses L and R.
        # Actually, I'll use S for number of headers, and 'h' for name
        self.root.S = 0
        self.root.N = 'h'
        self.root.L = self.root
        self.root.R = self.root

    def remove(self, node: DataObject, horizontal=True):
        if horizontal:
            node.R.L = node.L
            node.L.R = node.R
        else:
            node.U.D = node.D
            node.D.U = node.U
        #TODO, probaly should put this operation on a stack or something?



    #def restore(node: DataObject):

    #def cover(column: ColumnHeader):


    def search(self, k):
        """
        Our nondeterministic algorithm to find all exact covers can now be cast in the following
        explicit, deterministic form as a recursive procedure search(k), which is invoked initially
        with k = 0:
        """
        # If R[h] = h, print the current solution (see below) and return.
        if self.root.R == self.root:
            #TODO print the solution
            return
        
        # Find the column c with the least number of 1s (smallest size (S))
        c = self.root.R
        index = c
        while index != self.root:
            if index.S < c.S:
                c = index
            index = index.R
        
        # c is now the ColumnHeader with the least 1s
        # Cover column c ...



    # In this context, a row represents a subset that can be part of the solution
    # We will focus on adding rows, because a single row has meaning, whereas a single
    # column means little without the context of rows.  TODO is this true?
    def add_row(self, row):
        # Take in a size n array of 0s and 1s representing column 1-n
        # We need len(row) ColumnHeader()s to the right of root, make sure we have that
        while len(row) > self.root.S:
            self.add_column_header()
        
        # For each 1 in this row, add a DataObject to the end of the specified column
        # Bring a header index along so we can just add it as we go
        # Also keep track of the first and last DataObject in the row so we can link tail to head
        first = None
        last = None
        header_index = self.root.R # This is column A
        for data in row:
            if data == 1: # 1 here indicates the column is occupied
                # Add to the end of header_index
                # Reord last node in this row and potentially first if this is the first node
                last = self.add_to_bottom(header_index, last)
                if first == None:
                    first = last
            header_index = header_index.R
        if (first is not None) and (last is not None):
            first.L = last
            last.R = first


    def add_to_bottom(self, header: ColumnHeader, last: DataObject):
        new_node = DataObject()
        new_node.C = header
        new_node.D = header
        new_node.U = header.U
        header.U.D = new_node
        header.U = new_node

        if last is not None:
            new_node.L = last
            last.R = new_node
        new_node.C.S = new_node.C.S + 1
        return new_node

    def add_column_header(self):
        # We always add column headers to the right
        new_header = ColumnHeader()
        new_header.R = self.root
        new_header.L = self.root.L
        self.root.L.R = new_header
        self.root.L = new_header

        # Name this column header
        #TODO get_next_name should probably be a member function of the header class
        new_header.N = self.get_next_name(new_header)

        # Update the size of the header list
        self.root.S = self.root.S + 1 #TODO See if this works with ++

        # Initialize the header size
        new_header.S = 0

        # A new header will always point up and down to itself
        new_header.U = new_header
        new_header.D = new_header

    def get_next_name(self, header):
        # 1st case
        if header.L == self.root:
            return("A")
        else:
            prev_name = header.L.N
            return(chr(ord(prev_name) + 1))
            # TODO handle cases greater than z
            #if prev_name[-1] == "Z":
            #    try:
            #    if len(prev_name) == 1:
            #        header.N = "AA"






    


"""
The dance steps. One good way to implement algorithm X is to represent each 1 in the
matrix A as a data object x with five fields L[x], R[x], U[x], D[x], C[x]. Rows of the matrix
are doubly linked as circular lists via the L and R fields (“left” and “right”); columns are
doubly linked as circular lists via the U and D fields (“up” and “down”). Each column
list also includes a special data object called its list header.

The list headers are part of a larger object called a column object. Each column object y 
contains the fields L[y], R[y], U[y], D[y], and C[y] of a data object and two additional
fields, S[y] (“size”) and N[y] (“name”); the size is the number of 1s in the column, and the
name is a symbolic identifier for printing the answers. The C field of each object points
to the column object at the head of the relevant column.

The L and R fields of the list headers link together all columns that still need to be
covered. This circular list also includes a special column object called the root, h, which
serves as a master header for all the active headers. The fields U[h], D[h], C[h], S[h], and
N[h] are not used.

For example, the 0-1 matrix of (3) would be represented by the objects shown in
Figure 2, if we name the columns A, B, C, D, E, F, and G. (This diagram “wraps around”
toroidally at the top, bottom, left, and right. The C links are not shown because they
would clutter up the picture; each C field points to the topmost element in its column.)
Our nondeterministic algorithm to find all exact covers can now be cast in the following
explicit, deterministic form as a recursive procedure search(k), which is invoked initially
with k = 0:

If R[h] = h, print the current solution (see below) and return.
Otherwise choose a column object c (see below).
Cover column c (see below).
For each r ← D[c], D[D[c]], . . . , while r != c,
    set Ok ← r;
    for each j ← R[r], R[R[r]], . . . , while j != r,
        cover column j (see below);
    search(k + 1);
    set r ← Ok and c ← C[r];
    for each j ← L[r], L[L[r]], . . . , while j != r,
        uncover column j (see below).
Uncover column c (see below) and return.

The operation of printing the current solution is easy: We successively print the rows
containing O0, O1, . . . , Ok−1, where the row containing data object O is printed by
printing N[C[O]], N[C[R[O]]], N[C[R[R[O]]]], etc.
"""