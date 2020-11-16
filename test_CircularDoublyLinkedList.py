from DoublyLinkedList import CircularDoublyLinkedList

def verify_is_circular(CDLL):
    if CDLL.start_node is None:
        # An empty list is circular I guess
        return
    head = CDLL.start_node
    tail = CDLL.start_node.prev
    assert head.prev == tail
    assert tail.next == head

    full_list = CDLL.traverse_list()
    assert head.data == full_list[0]
    assert tail.data == full_list[-1]


def test_CDLL_insert_in_empty_list():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_in_emptylist(1)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

    CDLL.insert_in_emptylist(10)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

def test_CDLL_insert_at_start():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_start(1)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

    CDLL.insert_at_start(2)
    actual = CDLL.traverse_list()
    assert actual == [2, 1]
    verify_is_circular(CDLL)

    CDLL.insert_at_start(2)
    actual = CDLL.traverse_list()
    assert actual == [2, 2, 1]
    verify_is_circular(CDLL)

    CDLL.insert_at_start(3)
    actual = CDLL.traverse_list()
    assert actual == [3, 2, 2, 1]
    verify_is_circular(CDLL)

def test_CDLL_insert_at_end():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

    CDLL.insert_at_end(2)
    actual = CDLL.traverse_list()
    assert actual == [1, 2]
    verify_is_circular(CDLL)

    CDLL.insert_at_end(2)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 2]
    verify_is_circular(CDLL)

    CDLL.insert_at_end(3)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 2, 3]
    verify_is_circular(CDLL)

def test_CDLL_insert_after_item():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

    CDLL.insert_after_item(1, 10)
    actual = CDLL.traverse_list()
    assert actual == [1, 10]
    verify_is_circular(CDLL)

    CDLL.insert_after_item(1, 5)
    actual = CDLL.traverse_list()
    assert actual == [1, 5, 10]
    verify_is_circular(CDLL)

    CDLL.insert_after_item(1, 2)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 5, 10]
    verify_is_circular(CDLL)

    CDLL.insert_after_item(5, 6)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 5, 6, 10]
    verify_is_circular(CDLL)

    CDLL.insert_after_item(10, 11)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 5, 6, 10, 11]
    verify_is_circular(CDLL)

def test_CDLL_insert_before_item():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(10)
    actual = CDLL.traverse_list()
    assert actual == [10]
    verify_is_circular(CDLL)

    CDLL.insert_before_item(10, 1)
    actual = CDLL.traverse_list()
    assert actual == [1, 10]
    verify_is_circular(CDLL)

    CDLL.insert_before_item(10, 5)
    actual = CDLL.traverse_list()
    assert actual == [1, 5, 10]
    verify_is_circular(CDLL)

    CDLL.insert_before_item(1, 0)
    actual = CDLL.traverse_list()
    assert actual == [0, 1, 5, 10]
    verify_is_circular(CDLL)

    CDLL.insert_before_item(5, 4)
    actual = CDLL.traverse_list()
    assert actual == [0, 1, 4, 5, 10]
    verify_is_circular(CDLL)

    CDLL.insert_before_item(10, 9)
    actual = CDLL.traverse_list()
    assert actual == [0, 1, 4, 5, 9, 10]
    verify_is_circular(CDLL)

def test_CDLL_delete_at_end():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    CDLL.insert_at_end(2)
    CDLL.insert_at_end(3)
    CDLL.insert_at_end(4)
    CDLL.insert_at_end(5)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 3, 4, 5]
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 3, 4]
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 3]
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == [1, 2]
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)

    CDLL.delete_at_end()
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)

def test_CDLL_delete_element_by_value():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    CDLL.insert_at_end(2)
    CDLL.insert_at_end(3)
    CDLL.insert_at_end(4)
    CDLL.insert_at_end(5)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 3, 4, 5]
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(3)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 4, 5]
    verify_is_circular(CDLL) 

    CDLL.delete_element_by_value(1)
    actual = CDLL.traverse_list()
    assert actual == [2, 4, 5]
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(5)
    actual = CDLL.traverse_list()
    assert actual == [2, 4]
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(2)
    actual = CDLL.traverse_list()
    assert actual == [4]
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(2)
    actual = CDLL.traverse_list()
    assert actual == [4]
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(4)
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)

    CDLL.delete_element_by_value(4)
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)

def test_CDLL_reverse_linked_list_more_than_2():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    CDLL.insert_at_end(2)
    CDLL.insert_at_end(3)
    CDLL.insert_at_end(4)
    CDLL.insert_at_end(5)
    CDLL.insert_at_end(6)
    actual = CDLL.traverse_list()
    assert actual == [1, 2, 3, 4, 5, 6]        
    verify_is_circular(CDLL)
    CDLL.reverse_linked_list()
    actual = CDLL.traverse_list()
    assert actual == [6, 5, 4, 3, 2, 1]
    verify_is_circular(CDLL)

def test_CDLL_reverse_linked_list_exactly_2():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    CDLL.insert_at_end(2)
    actual = CDLL.traverse_list()
    assert actual == [1, 2]
    verify_is_circular(CDLL)
    CDLL.reverse_linked_list()
    actual = CDLL.traverse_list()
    assert actual == [2, 1]
    verify_is_circular(CDLL)

def test_CDLL_reverse_linked_list_exactly_1():
    CDLL = CircularDoublyLinkedList()
    CDLL.insert_at_end(1)
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)
    CDLL.reverse_linked_list()
    actual = CDLL.traverse_list()
    assert actual == [1]
    verify_is_circular(CDLL)

def test_CDLL_reverse_linked_list_empty():
    CDLL = CircularDoublyLinkedList()
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)
    CDLL.reverse_linked_list()
    actual = CDLL.traverse_list()
    assert actual == []
    verify_is_circular(CDLL)