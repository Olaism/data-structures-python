import unittest
from node import Node
from linkedlist import LinkedList


class NodeTest(unittest.TestCase):

    def test_node_instance(self):
        node = Node(300)
        self.assertIsInstance(node, Node)

    def test_node_data(self):
        node = Node(400)
        self.assertEqual(node.data, 400)
        self.assertNotEqual(node.data, 300)

    def test_node_ref(self):
        node = Node(200)
        self.assertIsNone(node.ref)

    def test_valid_node_ref(self):
        node = Node(200)
        node.ref = 'foo'
        self.assertEqual(node.ref, 'foo')


if __name__ == '__main__':
    unittest.main()
