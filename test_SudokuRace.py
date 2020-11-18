from SudokuSolver import Sudoku
from SudokuSolverDict import solve_sudoku
def test_SudokuSolver_Sudoku_race():
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
    #sudoku.print_state()
    sudoku.get_solution()
    sudoku.update_state()
    print()
    sudoku.print_state()

def test_SudokuSolver_Sudoku_dict_race():
    grid = [
        [5, 0, 0, 0, 8, 0, 0, 4, 9],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 6, 7, 3, 0, 0, 0, 0, 1],
        [1, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 8],
        [7, 0, 0, 0, 0, 4, 1, 5, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [4, 9, 0, 0, 5, 0, 0, 0, 3]]
    print()
    for solution in solve_sudoku((3, 3), grid):
        print(*solution, sep='\n')