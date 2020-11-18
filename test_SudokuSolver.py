import pytest
import random
from SudokuSolver import indicies_to_row, blank_sudoku, Sudoku, get_point_from_constraint, get_constraints_from_point

def test_SudokuSolver_indicies_to_row():
    i1 = random.randint(0, 324)
    i2 = random.randint(0, 324)
    i3 = random.randint(0, 324)
    i4 = random.randint(0, 324)
    row = indicies_to_row([i1, i2, i3, i4])
    assert row[i1] == 1
    assert row[i2] == 1
    assert row[i3] == 1
    assert row[i4] == 1
    assert sum(row) == 4
    assert len(row) == 324

def test_SudokuSolver_blank_sudoku():
    sudoku = blank_sudoku()
    assert sudoku.root.S == 324
    assert sudoku.root.L.N == "323" #0 indexed Ugh
    assert sudoku.root.R.N == "0"
    header_index = sudoku.root.R
    header_name = "0"
    while header_index != sudoku.root:
        assert header_index.S == 9
        assert header_index.N == header_name
        header_name = str(int(header_name) + 1)
        header_index = header_index.R

def test_SudokuSolver_Sudoku_init():
    sudoku = Sudoku()
    assert sudoku.root.S == 324
    assert sudoku.root.L.N == "323"
    assert sudoku.root.R.N == "0"
    header_index = sudoku.root.R
    header_name = "0"
    while header_index != sudoku.root:
        assert header_index.S == 9
        assert header_index.N == header_name
        header_name = str(int(header_name) + 1)
        header_index = header_index.R      
    print(sudoku.state) 

def test_SudokuSolver_Sudoku_add_clue():
    sudoku = Sudoku()
    sudoku.print_state()
    clue = (1, 1, 5)
    sudoku.add_clue(clue)
    sudoku.print_state() 
    assert sudoku.state[clue[0] - 1][clue[1] - 1] == clue[2]
    total = sum([sum(row) for row in sudoku.state])
    assert total == clue[2]

def test_SudokuSolver_Sudoku_add_clues():
    sudoku = Sudoku()
    clues = [
        (1, 1, 5),
        (1, 5, 8),
        (1, 8, 4),
        (1, 9, 9),
        (2, 4, 5),
        (2, 8, 3),
        (3, 2, 6),
        (3, 3, 7),
        (3, 4, 3),
        (3, 9, 1),
        (4, 1, 1),
        (4, 2, 5),
        (5, 4, 2),
        (5, 6, 8),
        (6, 8, 1),
        (6, 9, 8),
        (7, 1, 7),
        (7, 6, 4),
        (7, 7, 1),
        (7, 8, 5),
        (8, 2, 3),
        (8, 6, 2),
        (9, 1, 4),
        (9, 2, 9),
        (9, 5, 5),
        (9, 9, 3)
    ]
    sudoku.add_clues(clues)
    sudoku.print_state() 
    for clue in clues:
        assert sudoku.state[clue[0] - 1][clue[1] - 1] == clue[2]


def test_SudokuSolver_Sudoku_get_point_from_constraint():
    point = (random.randint(1, 9), \
             random.randint(1, 9), \
             random.randint(1, 9))
    print(point)
    constraints = get_constraints_from_point(point)
    print(constraints)
    actual = get_point_from_constraint(constraints)
    print(actual)
    assert actual == point

@pytest.mark.parametrize(
    "constraints, point", 
    [
    ([0,  81,  162, 243], (1, 1, 1)),
    ([1,  82,  163, 243], (1, 1, 2)),
    ([2,  83,  164, 243], (1, 1, 3)),
    ([80, 161, 242, 323], (9, 9, 9)),
])
def test_SudokuSolver_Sudoku_get_point_from_constraint_param(constraints, point):
    actual = get_point_from_constraint(constraints)
    print(actual)
    assert actual == point

@pytest.mark.parametrize(
    "constraints, point", 
    [
    ([0,  81,  162, 243], (1, 1, 1)),
    ([1,  82,  163, 243], (1, 1, 2)),
    ([2,  83,  164, 243], (1, 1, 3)),
    ([80, 161, 242, 323], (9, 9, 9)),
])
def test_SudokuSolver_Sudoku_get_constraints_from_point_param(constraints, point):
    actual = get_constraints_from_point(point)
    print(actual)
    assert actual ==  constraints

def test_SudokuSolver_Sudoku_solve_blank():
    sudoku = Sudoku()
    sudoku.solve()
    sudoku.print_state()
    sudoku.get_solution()
    sudoku.update_state()
    sudoku.print_state()

def test_SudokuSolver_Sudoku_solve():
    sudoku = Sudoku()
    clues = [
        (1, 1, 5),
        (1, 5, 8),
        (1, 8, 4),
        (1, 9, 9),
        (2, 4, 5),
        (2, 8, 3),
        (3, 2, 6),
        (3, 3, 7),
        (3, 4, 3),
        (3, 9, 1),
        (4, 1, 1),
        (4, 2, 5),
        (5, 4, 2),
        (5, 6, 8),
        (6, 8, 1),
        (6, 9, 8),
        (7, 1, 7),
        (7, 6, 4),
        (7, 7, 1),
        (7, 8, 5),
        (8, 2, 3),
        (8, 6, 2),
        (9, 1, 4),
        (9, 2, 9),
        (9, 5, 5),
        (9, 9, 3)
    ]
    sudoku.add_clues(clues)
    sudoku.solve()
    sudoku.print_state()
    sudoku.get_solution()
    sudoku.update_state()
    sudoku.print_state()