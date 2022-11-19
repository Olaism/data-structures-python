import unittest
from node import Node
from linkedlist import LinkedList


class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = Node(300)

    def test_node_instance(self):
        node = self.node
        self.assertIsInstance(node, Node)

    def test_node_data(self):
        self.assertEqual(self.node.data, 300)
        self.assertNotEqual(self.node.data, 200)

    def test_node_ref(self):
        self.assertIsNone(self.node.ref)

    def test_valid_node_ref(self):
        self.node.ref = 'foo'
        self.assertEqual(self.node.ref, 'foo')


class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.node = Node(400)
        self.llist = LinkedList()

    def test_list_instance(self):
        self.assertIsInstance(self.llist, LinkedList)

    def test_list_no_data(self):
        self.assertEqual(self.llist.datas(), [])

    def test_list_head(self):
        self.llist.head = self.node
        self.assertTrue(self.llist.has_header())
        self.assertEqual(self.llist.datas(), [400])

    def test_add_left_method(self):
        self.llist.head = self.node
        self.llist.add_left(300)
        self.assertTrue(self.llist.has_header())
        self.assertEqual(self.llist.head.data, 300)
        self.assertEqual(self.llist.datas(), [300, 400])

    def test_add_right_method(self):
        self.llist.head = self.node
        self.llist.add_right(300)
        self.assertTrue(self.llist.has_header())
        self.assertEqual(self.llist.get_last_element().data, 300)
        self.assertEqual(self.llist.datas(), [400, 300])


if __name__ == '__main__':
    unittest.main()
