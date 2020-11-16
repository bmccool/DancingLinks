from DoublyLinkedList import DataObject, ColumnHeader, ColumnObject
import pytest

@pytest.fixture
def fig_2():
    fig2 = ColumnObject()
    fig2.add_row([0, 0, 1, 0, 1, 1, 0]) #TODO This guy is not updating ColumnHeader('C').D
    fig2.add_row([1, 0, 0, 1, 0, 0, 1])
    fig2.add_row([0, 1, 1, 0, 0, 1, 0])
    fig2.add_row([1, 0, 0, 1, 0, 0, 0])
    fig2.add_row([0, 1, 0, 0, 0, 0, 1])
    fig2.add_row([0, 0, 0, 1, 1, 0, 1])
    yield fig2

def check_row(matrix: ColumnObject, labels, depth):
    if len(labels) == 0:
        return True
    else:
        # Grab the first node to check.  It should be at the first label in labels, depth nodes down
        # Move the header index to the first label in "labels"
        print("CHECKING SIZES")
        header_index = matrix.root
        while header_index.N != labels[0]:
            header_index = header_index.R
        for _ in range(depth):
            header_index = header_index.D
        # header index should now point to the first node in the row by going (depth) nodes below the first label
        # Go through the labels, and verify nodes are as listed.  Verify forwards and backwards wrapping
        for label in labels:
            assert header_index.C.N == label
            header_index = header_index.R
        # This should have wrapped to index 0
        assert header_index.C.N == labels[0]
        # Wrap around the left to the right
        header_index = header_index.L
        assert header_index.C.N == labels[-1]
        # Verify in reverse order
        for label in reversed(labels):
            assert header_index.C.N == label
            header_index = header_index.L

def check_fig_2_whole(fig_2: ColumnObject):
    # Check Labels (names)
    header_index = fig_2.root
    row = [header_index.N] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.N)
    assert row == ['h', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

    # Check Sizes
    header_index = fig_2.root
    row = [header_index.S] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.S)
    assert row == [7, 2, 2, 2, 3, 2, 2, 3]

    # Check Row 1
    check_row(fig_2, ['C', 'E', 'F'], 1)
    # Check Row 2
    check_row(fig_2, ['A', 'D', 'G'], 1)
    # Check Row 3
    check_row(fig_2, ['B', 'C', 'F'], 1)
    # Check Row 4
    check_row(fig_2, ['A', 'D'], 2)
    # Check Row 5
    check_row(fig_2, ['B', 'G'], 2)
    # Check Row 6
    check_row(fig_2, ['D', 'E', 'G'], 3)    

def check_fig_2_cover_a(fig_2: ColumnObject):
    # Check Labels (names)
    header_index = fig_2.root
    row = [header_index.N] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.N)
    assert row == ['h', 'B', 'C', 'D', 'E', 'F', 'G']

    # Check Sizes
    header_index = fig_2.root
    row = [header_index.S] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.S)
    assert row == [6, 2, 2, 1, 2, 2, 2]

    # Check Row 1
    check_row(fig_2, ['C', 'E', 'F'], 1)
    # Check Row 2 BUT COL A IS GONE
    # check_row(fig_2, ['A'], 1)
    # Check Row 3
    check_row(fig_2, ['B', 'C', 'F'], 1)
    # Check Row 4 # BUT COL A IS GONE
    #check_row(fig_2, ['A'], 2)
    # Check Row 5
    check_row(fig_2, ['B', 'G'], 2)
    # Check Row 6
    check_row(fig_2, ['D', 'E', 'G'], 1)    

def test_fig_2_creation(fig_2):
    check_fig_2_whole(fig_2)

def test_fig_2_removal(fig_2):
    header_index = fig_2.root

    # Remove header A horiz
    header_index = header_index.R
    header_index.remove()
    
    # From A, down, right, remove vert
    header_index = header_index.D.R
    header_index.remove()

    # From there, right, remove vert
    header_index = header_index.R
    header_index.remove()

    # From A, down, down, right, remove vert
    header_index = header_index.R.D.R
    header_index.remove()

    check_fig_2_cover_a(fig_2)

def test_fig_2_restore(fig_2):
    remove_index = fig_2.root

    # Remove header A horiz
    remove_index = remove_index.R
    remove_index.remove()
    
    # From A, down, right, remove vert
    remove_index = remove_index.D.R
    remove_index.remove()

    # From there, right, remove vert
    remove_index = remove_index.R
    remove_index.remove()

    # From A, down, down, right, remove vert
    remove_index = remove_index.R.D.R
    remove_index.remove()

    check_fig_2_cover_a(fig_2)

    # Restore in reverse order...
    restore_index = remove_index

    #header_index = header_index.R.D.R
    #fig_2.remove(header_index, False)
    restore_index.restore()
    restore_index = restore_index.L.U.L

    #header_index = header_index.R
    #fig_2.remove(header_index, False)
    restore_index.restore()
    restore_index = restore_index.L

    #header_index = header_index.D.R
    #fig_2.remove(header_index, False)
    restore_index.restore()
    restore_index = restore_index.L.U

    # Remove header A horiz
    #header_index = header_index.R
    #fig_2.remove(header_index)
    restore_index.restore()
    remove_index = remove_index.L # Just point back to root at this point
    
    check_fig_2_whole(fig_2)

def test_DLX_cover_fig_2(fig_2):
    header_index = fig_2.root

    # Cover Column A
    header_index = header_index.R
    header_index.cover()

    check_fig_2_cover_a(fig_2)

def test_DLX_uncover_fig_2(fig_2):
    header_index = fig_2.root

    # Cover Column A
    column_a = header_index.R
    column_a.cover()

    check_fig_2_cover_a(fig_2)  

    # Uncover Column A
    column_a.uncover()

    check_fig_2_whole(fig_2)

def test_DLX_search_fig_2(fig_2):
    fig_2.search(0)
    assert fig_2.solution[0] == ["A", "D"]
    assert fig_2.solution[1] == ["E", "F", "C"]
    assert fig_2.solution[2] == ["B", "G"]
    # This shows that fig 2 has an exact cover with:
    #    Row 4(A,D)
    #    Row 1(C, E, F)
    #    Row 5(B, G)