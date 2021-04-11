import unittest
from AVLTree import AVLTree, Node


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree(Node(2))
        self.tree.insert(1)

    def test_creation(self):
        self.assertEqual(2, self.tree.root.value)
        self.assertTrue(self.tree.is_balanced(self.tree.root))

    def test_insert1(self):
        self.tree.insert(0)
        self.assertEqual(1, self.tree.root.value)
        self.assertTrue(self.tree.is_balanced(self.tree.root))

    def test_insert2(self):
        self.tree.insert(0)
        self.tree.insert(3)
        self.tree.insert(4)
        self.assertEqual(1, self.tree.root.value)
        self.assertEqual(2, self.tree.height(self.tree.root))
        self.assertTrue(self.tree.is_balanced(self.tree.root))

    def test_insert3(self):
        self.tree.insert(0)
        self.tree.insert(3)
        self.tree.insert(4)
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(6)
        self.assertEqual(2, self.tree.root.value)
        self.assertEqual(5, self.tree.root.right_child.right_child.value)
        self.assertEqual(3, self.tree.height(self.tree.root))
        self.assertTrue(self.tree.is_balanced(self.tree.root))


if __name__ == '__main__':
    unittest.main()
