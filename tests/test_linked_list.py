import unittest
from data_structures.linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning(5)
        ll.insert_beginning(10)
        self.assertEqual(ll.get_head_node().get_value(), 10)

if __name__ == '__main__':
    unittest.main()