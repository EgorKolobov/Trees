import unittest
from SplayTree import SplayTree, Node


class SplayTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = SplayTree(Node(4))
        self.tree.insert(2)
        self.tree.insert(6)
        self.tree.insert(3)
        self.tree.insert(5)

    def test_creation(self):
        self.assertEqual(5, self.tree.root.value)

    def test_search(self):
        result_node = self.tree.search_node(3)
        self.assertEqual(3, result_node.value)
        self.assertEqual(self.tree.root.value, result_node.value)
        self.assertEqual(2, result_node.left_child.value)
        self.assertEqual(5, result_node.right_child.value)

    def test_remove(self):
        self.tree.remove(3)
        self.assertEqual(4, self.tree.root.value)
        self.assertEqual(2, self.tree.root.left_child.value)
        self.assertEqual(5, self.tree.root.right_child.value)
        self.assertEqual(6, self.tree.root.right_child.right_child.value)
        self.assertEqual(None, self.tree.search_node(3))


if __name__ == '__main__':
    unittest.main()
