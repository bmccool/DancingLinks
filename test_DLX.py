from DLX import DataObject, ColumnHeader, DLXObject
import pytest

@pytest.fixture
def fig_2():
    fig2 = DLXObject()
    fig2.add_row([0, 0, 1, 0, 1, 1, 0]) #TODO This guy is not updating ColumnHeader( '3').D
    fig2.add_row([1, 0, 0, 1, 0, 0, 1])
    fig2.add_row([0, 1, 1, 0, 0, 1, 0])
    fig2.add_row([1, 0, 0, 1, 0, 0, 0])
    fig2.add_row([0, 1, 0, 0, 0, 0, 1])
    fig2.add_row([0, 0, 0, 1, 1, 0, 1])
    yield fig2

def check_row(matrix: DLXObject, labels, depth):
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

def check_fig_2_whole(fig_2: DLXObject):
    # Check Labels (names)
    header_index = fig_2.root
    row = [header_index.N] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.N)
    assert row == ['h', '0', '1', '2', '3', '4', '5', '6']

    # Check Sizes
    header_index = fig_2.root
    row = [header_index.S] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.S)
    assert row == [7, 2, 2, 2, 3, 2, 2, 3]

    # Check Row 1
    check_row(fig_2, [ '2', '4', '5'], 1)
    # Check Row 2
    check_row(fig_2, ['0', '3', '6'], 1)
    # Check Row 3
    check_row(fig_2, ['1', '2', '5'], 1)
    # Check Row 4
    check_row(fig_2, ['0', '3'], 2)
    # Check Row 5
    check_row(fig_2, ['1', '6'], 2)
    # Check Row 6
    check_row(fig_2, ['3', '4', '6'], 3)    

def check_fig_2_cover_a(fig_2: DLXObject):
    # Check Labels (names)
    header_index = fig_2.root
    row = [header_index.N] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.N)
    assert row == ['h', '1', '2', '3', '4', '5', '6']

    # Check Sizes
    header_index = fig_2.root
    row = [header_index.S] # Get the first one
    while header_index.R != fig_2.root:
        header_index = header_index.R
        row.append(header_index.S)
    assert row == [6, 2, 2, 1, 2, 2, 2]

    # Check Row 1
    check_row(fig_2, [ '2', '4', '5'], 1)
    # Check Row 2 BUT COL A IS GONE
    # check_row(fig_2, ['1'], 1)
    # Check Row 3
    check_row(fig_2, ['1', '2', '5'], 1)
    # Check Row 4 # BUT COL A IS GONE
    #check_row(fig_2, ['1'], 2)
    # Check Row 5
    check_row(fig_2, ['1', '6'], 2)
    # Check Row 6
    check_row(fig_2, ['3', '4', '6'], 1)    

def test_DLX_creation_fig_2(fig_2):
    check_fig_2_whole(fig_2)

def test_DLX_removal_fig_2(fig_2):
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

def test_DLX_restore_fig_2(fig_2):
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
    assert fig_2.solution[0] == ['0', '3']
    assert fig_2.solution[1] == ['4', '5', '2']
    assert fig_2.solution[2] == ['1', '6']
    assert len(fig_2.solution) == 3
    # This shows that fig 2 has an exact cover with:
    #    Row 4['0', '3']
    #    Row 1['4', '5', '2']
    #    Row 5['1', '6']

def test_DLX_given_1(fig_2):
    fig_2.given(['0', '3'])
    fig_2.search(0)
    assert fig_2.solution[0] == ['4', '5', '2']
    assert fig_2.solution[1] == ['1', '6']
    assert len(fig_2.solution) == 2

def test_DLX_given_2(fig_2):
    fig_2.given(['0', '3'])
    fig_2.given(['4', '5', '2'])
    fig_2.search(0)
    assert fig_2.solution[0] == ['1', '6']
    assert len(fig_2.solution) == 1