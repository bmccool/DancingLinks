from DLX import DLXObject

rows = [
    " 42 3   1",
    "856  7   ",
    "  1 2  4 ",
    " 6927 48",
    "  4   2  ",
    " 83 4156 ",
    " 1  8 3  ",
    "   1  724",
    "6   9 15 ",

]

problem_1 = [
    [' ', '4', '2', ' ', '3', ]
]

class Sudoku(DLXObject):
    """
    The easiest way to input a sudoko information is probably in a (row, col, val) 3-tuples, 
    but it is probably easiest to store multiples of this information in a 2d list.
    So we will have a class Sudoko that stores data as a 2d list, but takes in information
    as a single triplet.
    """
    def __init__(self):
        super().__init__()
        blank_sudoku(self) # Initialize all the constraints and choices of the DLXObject
        self.state = [0] * 9 # Hold the current state (all active choices) of the puzzle
        for row in range(9):
            self.state[row] = [0] * 9

    def solve(self):
        self.search(stop=True)

    def update_state(self):
        self.get_solution()
        for row in self.solution:
            for index, data in enumerate(row):
                row[index] = int(data)
            row.sort()
            point = get_point_from_constraint(row)
            self.state[point[0] - 1][point[1] - 1] = point[2]

    def add_clues(self, clues: list):
        # Add given clues to the puzzle in (row, col, val) 3-tuples
        for clue in clues:
            self.add_clue((clue[0], clue[1], clue[2]))

    def add_clue(self, clue):
        # Add given clue to the puzzle in (row, col, val) 3-tuples
        # A clue corresponds to a row, and to 'activate' that row, we need
        # to cover all the constraints in that row.
        constraints = get_constraints_from_point(clue)
        #TODO should DLX just accept a list of ints?  We already keep column headers as str(int)s...
        constraints = [str(data) for data in constraints] # Header names are strings of ints

        # Add the constraints as a given
        self.given(constraints)

        # Add the clue to our state
        self.state[clue[0] - 1][clue[1] - 1] = clue[2]

    def print_state(self):
        print("+-----+-----+-----+")
        for index, row in enumerate(self.state):
            line = "|" + " ".join(map(str, row[0:3])) + \
                   "|" + " ".join(map(str, row[3:6])) + \
                   "|" + " ".join(map(str, row[6:9])) + "|"
            print(line)
            if (index % 3) == 2:
                 print("+-----+-----+-----+")



def sudoku_to_dlx(rows: list):
    """ 
    'sudoko' means a 2d list (left to right, top to bottom) 9x9.
    'dlx' means a representation in which there are 324 contraints (headers)
    and 729 rows representing each possible location/value combination
    Explained:
    Each row must have 9 values in it and there are 9 rows       81
    Each column must have 9 values in it and there are 9 columns 81
    Each box must have 9 values in it and there are 9 boxes      81
    Each cell must have a value in it and there are 9x9 cells  + 81 = 324 constraints
    9 possible row locations, 
    9 possible column locations, 
    9 possible values = 729 possible placements
    
    So what we really need is a mapping of 'There's a 7 in row,col==(2,3)' to 
    each of the constraints it fulfills.

    We should pick a coordinate convention for the suduko puzzle.  It shouldn't
    matter but we will call rows top to bottom, columns left to right.  Cells
    then are numbered left to right, top to bottom, like a book.

    Our interface into dlx is feeding rows at a time represented as a list with 0s
    and 1s.  This is obviously not great, so we'll need a helper function to 
    create that list by passing the indexes of the contsraints and spitting out
    the row.  TODO maybe we should modify dlx to take this 'indexed' format too?

    """
    return

def get_constraints_from_point(point):
    row = point[0]
    col = point[1]
    val = point[2]

    if (row < 1 or row > 9) or \
       (col < 1 or col > 9) or \
       (val < 1 or val > 9):
       raise ValueError("Points should be [1-9]! Point given: {}".format(str(point)))
    
    # There is an index for row, col, box, and cell
        
    # Row constraints - one of 1-9 in each row
    # Row 1 (1-9) Row 2 (1-9) ... Row 9 (1-9) == 81
    row_index = ((row - 1) * 9 ) + (val - 1) 

    # Col constraints - one of 1-9 in each col
    # Col 1 (1-9) Col 2 (1-9) ... Col 9 (1-9) == 81
    col_index = ((col - 1) * 9) + (val -1) + 81

    # Box constraints - one of 1-9 in each box
    # Box 1 (1-9) Box 2 (1-9) ... Box 9 (1-9) == 81
    # How to know which box this is in though?
    # TODO there's probably an easier way to do this...
    if row < 4:
        if col < 4:
            box = 1
        elif col < 7:
            box = 4
        else:
            box = 7
    elif row < 7:
        if col < 4:
            box = 2
        elif col < 7:
            box = 5
        else:
            box = 8
    else:
        if col < 4:
            box = 3
        elif col < 7:
            box = 6
        else:
            box = 9
    box_index = ((box - 1) * 9) + (val - 1) + 81 + 81

    # Cell constraints - Only one thing in any given box
    cell_index = ((row - 1) * 9) + (col - 1) + 81 + 81 + 81
        
    return [row_index, col_index, box_index, cell_index]    

def get_point_from_constraint(constraint):
    # constraint is row, col, box, cell
    # row, col, or box will tell us what the value is
    # cell will tell us the location
    row_index = constraint[0]
    col_index = constraint[1]
    box_index = constraint[2]
    cell_index = constraint[3]

    # Cell constraints - Only one thing in any given box
    # 0-index cell_index... This doesn't really matter, 81 is divisible by 9
    cell_index = cell_index - 81 - 81 - 81
    col = (cell_index % 9) + 1
    row = (int(cell_index / 9)) + 1

    # get val from row...
    # row_index = ((row - 1) * 9 ) + (val - 1)
    #   val = row_index - ((row - 1) * 9 ) + 1
    row_val = row_index - ((row - 1) * 9 ) + 1

    # Double check val from col...
    # col_index =       ((col - 1) * 9) + (val -1) + 81
    #   val = col_index - ((col - 1) * 9) - 81 + 1
    col_val = col_index - ((col - 1) * 9) - 81 + 1
    if col_val != row_val:
        error = ["Value is not the same derived from row vs col!", \
                 "Derived row_val: {}".format(row_val), \
                 "Derived col_val: {}".format(col_val), \
                 "Inputs: {}".format(str(constraint))
            ]
        print(error)
        #TODO raise something specific
        raise ValueError(error)

    return(row, col, row_val)  
    


def blank_sudoku(sudoku: DLXObject=None) -> DLXObject:
    """ Returns a DLXObject with all constraints and choices associated with
    a suduko puzzle """
    if sudoku == None:
        sudoku = DLXObject()
    row = 1
    col = 1
    val = 1
    for i in range(0, 729):
        dlx_row = indicies_to_row(get_constraints_from_point((row, col, val)))
        sudoku.add_row(dlx_row)

        val = val + 1
        if val == 10:
            val = 1
            col = col + 1
            if col == 10:
                col = 1
                row = row + 1
                if row == 10:
                    break
    return sudoku
    

def indicies_to_row(indicies: list, pad=324):
    """ Convert a list of indicies to a list of 0s and 1s representing where 1
    represents where an index exists.  In this context we should only have 4 
    indicies, but we aren't going to check it here """
    row = [0] * 324
    for index in indicies:
        row[index] = 1

    return row
