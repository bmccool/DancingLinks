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

def test_fig_2_creation(fig_2):
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

def test_fig_2_removal(fig_2):
    header_index = fig_2.root

    # Remove header A horiz
    header_index = header_index.R
    fig_2.remove(header_index)
    
    # From A, down, right, remove vert
    header_index = header_index.D.R
    fig_2.remove(header_index, False)

    # From there, right, remove vert
    header_index = header_index.R
    fig_2.remove(header_index, False)

    # From A, down, down, right, remove vert
    header_index = header_index.R.D.R
    fig_2.remove(header_index, False)

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
    assert row == [7, 2, 2, 3, 2, 2, 3]

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