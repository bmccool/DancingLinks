class DataObject:
    def __init__(self):
        self.L = None # Left
        self.R = None # Right
        self.U = None # Up
        self.D = None # Down
        self.C = None # The C field of each object points to the column header at the head of the relevant column.

    def remove(self):
        self.U.D = self.D
        self.D.U = self.U
        self.C.S = self.C.S - 1

    def restore(self):
        self.U.D = self
        self.D.U = self
        self.C.S = self.C.S + 1

class ColumnHeader(DataObject):
    def __init__(self):
        # ColumnHeaders contain all the fields of a DataObject...
        super().__init__()
        # And two additional fields
        self.S = None #Size, Number of 1s in this column
        self.N = None #Name, symbolic identifies for printing answers

    def remove(self):
        self.R.L = self.L
        self.L.R = self.R
        self.C.S = self.C.S - 1

    def restore(self):
        self.R.L = self
        self.L.R = self
        self.C.S = self.C.S + 1

    def cover(self):
        # Remove this header
        self.remove()
        index = self
        index = index.D
        # For each DataObject in this column, remove all it's R peers, 
        # but NOT the one in this column
        while index != self:
            #this is a new row, remove all it's R peers
            column = index
            index = index.R
            while index != column:
                index.remove()
                index = index.R
            index = index.D

    def uncover(self):
        # Remove this header
        self.restore()
        index = self
        index = index.U
        # For each DataObject in this column, restore all it's L peers, 
        # but NOT the one in this column
        while index != self:
            #this is a new row, restore all it's L peers
            column = index
            index = index.L
            while index != column:
                index.restore()
                index = index.L
            index = index.U        

class DLXObject():
    #Meta object for DLX
    def __init__(self):
        self.root = ColumnHeader() # aka 'h', only uses L and R.
        # Actually, I'll use S for number of headers, and 'h' for name
        self.root.S = 0
        self.root.N = 'h'
        self.root.L = self.root
        self.root.R = self.root
        self.O = [] #TODO what does O represent?  Output? 
        self.solution = None

    def given(self, constraints: list):
        """
        This function will cover all the constraints listed, which can be
        thought of as starting with a 'given' choice that is already done
        """
        # Make sure constraints are strings that can match the header names
        for i,e in enumerate(constraints):
            constraints[i] = str(e)
        header_index = self.root.R
        while header_index != self.root:
            if header_index.N in constraints:
                header_index.cover()
            header_index = header_index.R


    def get_solution(self):
        rows = []
        for O in self.O:
            columns = [O.C.N]
            i = O.R
            while i != O:
                columns.append(i.C.N)
                i = i.R
            #print(columns)
            rows.append(columns)
        self.solution = rows
        # Storing the solution here will only store the "last" solution found
        # If we are interested in "all" solutions, this will need to be changed

    def search(self, k=0, stop=False):
        """
        Our nondeterministic algorithm to find all exact covers can now be cast in the following
        explicit, deterministic form as a recursive procedure search(k), which is invoked initially
        with k = 0:
        """
        # If R[h] = h, print the current solution (see below) and return.
        if self.root.R == self.root:
            print("FOUND A SOLUTION")
            self.get_solution()
            return True
        
        # Find the column c with the least number of 1s (smallest size (S))
        c = self.root.R
        index = c
        while index != self.root:
            if index.S < c.S:
                c = index
            index = index.R
        
        # c is now the ColumnHeader with the least 1s
        # Cover column c ...
        c.cover()

        # For each r ← D[c], D[D[c]], . . . , while r != c,
        r = c.D
        while r != c:
            # set Ok ← r;
            try:
                self.O[k] = r
            except:
                self.O.append(r)
                #TODO if we want to track choices as they are done, we just added choice r to self.O

            # for each j ← R[r], R[R[r]], . . . , while j != r,
            j = r.R
            while j != r:
                # cover column j (see below);
                j.C.cover()
                j = j.R

            # search(k + 1);
            retval = self.search(k + 1, stop)
            # If we want to stop after the first solution...
            if retval and stop:
                return True

            # set r ← Ok and c ← C[r];
            # TODO, these should already be set, right?
            r = self.O[k]
            c = r.C

            # for each j ← L[r], L[L[r]], . . . , while j != r,
            j = r.L
            while j != r:
                # uncover column j (see below).
                j.C.uncover()
                j = j.L

            r = r.D

        #Uncover column c (see below) and return.
        c.uncover()
        return False

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
        new_header.C = self.root # Just a helper to point all headers to root
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
            return("0")
        else:
            prev_name = header.L.N
            #return(chr(ord(prev_name) + 1))
            return(str(int(prev_name) + 1))
            # TODO handle cases greater than z
            #if prev_name[-1] == "Z":
            #    try:
            #    if len(prev_name) == 1:
            #        header.N = "AA"