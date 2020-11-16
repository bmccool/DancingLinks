from DoublyLinkedList import ColumnObject

def Alorithm_X(A: ColumnObject):
    """
    Algorithm X as described by Don Knuth, paper here:
        https://arxiv.org/pdf/cs/0011047.pdf
    Given a matrix, A, of 0s and 1s, find a subset of rows containing exactly 
    one 1 in each column.
    The algorithm is defined as:
        1. If A is empty, the problem is solved; terminate successfully.
            2. Otherwise, choose a column, c (deterministically).
                Optionally, choose c by the least number of 1s in the column
                If c is entirely 0, there is no solution; terminate unsuccessfully
            3. Choose a row, r, such that A[r, c] == 1 (nondeterministically).
            4. Include r in the partial solution.
            5. For each j such that A[r, j] == 1
                6. delete column j from matrix A;
                7. for each i susch that A[i, j] == 1,
                    8. delete row i from matrix A.
        9. Repeat this algorithm recursively on the reduced matrix A.
    """


