from dlx import DoublyLinkedList

def test_DLL_insert_in_empty_list():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_in_emptylist(50)
    actual = new_linked_list.traverse_list()
    assert actual == [50]

    new_linked_list.insert_in_emptylist(100)
    actual = new_linked_list.traverse_list()
    assert actual == [50]

def test_DLL_insert_at_start():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_start(10)
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_start(18)
    actual = new_linked_list.traverse_list()
    assert actual == [18, 5, 10]

def test_DLL_insert_at_end():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)
    actual = new_linked_list.traverse_list()
    assert actual == [10, 5, 18]    

def test_DLL_insert_after():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)
    new_linked_list.insert_after_item(10, 11)
    new_linked_list.insert_after_item(5, 6)
    new_linked_list.insert_after_item(18, 19)
    actual = new_linked_list.traverse_list()
    assert actual == [10, 11, 5, 6, 18, 19]

def test_DLL_insert_before():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)
    new_linked_list.insert_before_item(10, 9)
    new_linked_list.insert_before_item(5, 4)
    new_linked_list.insert_before_item(18, 17)
    actual = new_linked_list.traverse_list()
    assert actual == [9, 10, 4, 5, 17, 18]    

def test_DLL_delete_at_start():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)

    new_linked_list.delete_at_start()
    actual = new_linked_list.traverse_list()
    assert actual == [5, 18]    

    new_linked_list.delete_at_start()
    actual = new_linked_list.traverse_list()
    assert actual == [18]

    new_linked_list.delete_at_start()
    actual = new_linked_list.traverse_list()
    assert actual == []

    new_linked_list.delete_at_start()
    actual = new_linked_list.traverse_list()
    assert actual == []

def test_DLL_delete_at_end():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)

    new_linked_list.delete_at_end()
    actual = new_linked_list.traverse_list()
    assert actual == [10, 5]    

    new_linked_list.delete_at_end()
    actual = new_linked_list.traverse_list()
    assert actual == [10]    
 
    new_linked_list.delete_at_end()
    actual = new_linked_list.traverse_list()
    assert actual == []    

    new_linked_list.delete_at_end()
    actual = new_linked_list.traverse_list()
    assert actual == []    

def test_DLL_delete_by_value():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(18)

    new_linked_list.delete_element_by_value(5)
    actual = new_linked_list.traverse_list()
    assert actual == [10, 18]    

    new_linked_list.delete_element_by_value(5)
    actual = new_linked_list.traverse_list()
    assert actual == [10, 18]    

    new_linked_list.delete_element_by_value(10)
    actual = new_linked_list.traverse_list()
    assert actual == [18]    

    new_linked_list.delete_element_by_value(18)
    actual = new_linked_list.traverse_list()
    assert actual == []

    new_linked_list.delete_element_by_value(5)
    actual = new_linked_list.traverse_list()
    assert actual == []        

def test_DLL_reverse_linked_list():
    new_linked_list = DoublyLinkedList()
    new_linked_list.insert_at_end(1)
    new_linked_list.insert_at_end(2)
    new_linked_list.insert_at_end(3)
    new_linked_list.insert_at_end(4)
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(6)
    actual = new_linked_list.traverse_list()
    assert actual == [1, 2, 3, 4, 5, 6]        
    new_linked_list.reverse_linked_list()
    actual = new_linked_list.traverse_list()
    assert actual == [6, 5, 4, 3, 2, 1]        