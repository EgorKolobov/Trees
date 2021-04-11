from BaseTree import BaseTree, Node


class AVLTree(BaseTree):
    def __init__(self, root: Node = None, threshold: int = 1):
        super().__init__(root)
        if threshold < 1:
            raise Exception("__init__: threshold can't be lower than 1")
        self.threshold = threshold

    # returns the height of a subtree with root at some_node
    def height(self, some_node: Node) -> int:
        if some_node is None:
            return -1
        else:
            return max(self.height(some_node.left_child), self.height(some_node.right_child)) + 1

    # counts balance of a subtree(root=some_node): height(left subtree)-height(right subtree)
    def count_balance(self, some_node: Node) -> int:
        return self.height(some_node.left_child)-self.height(some_node.right_child)

    # inserts a new node with needed value to the tree
    def insert(self, value) -> None:
        self._check_balancing(super().insert(value))

    # cheks if tree is still balanced after new insertion
    def _check_balancing(self, some_node: Node, path=[]) -> None:
        if some_node.parent == None:
            return
        path += [some_node]

        # If current node is unbalanced (no matter how)
        if not self.is_balanced(some_node.parent):
            path += [some_node.parent]
            self._adjust_balance(path[-1], path[-2], path[-3])
            return

        self._check_balancing(some_node.parent, path)

    # checks if a subtree(root=some_node) is balanced
    def is_balanced(self, some_node: Node) -> bool:
        return abs(self.count_balance(some_node)) <= self.threshold

    # fixes balancing if tree is unbalanced. called in _check_balancing
    def _adjust_balance(self, parent: Node, node: Node, child: Node) -> None:
        # Zig-Zig case. Make one right turn.
        if node == parent.left_child and child == node.left_child:
            self._right_rotate(parent)
        # Zag-Zag case. Make one left turn.
        elif node == parent.right_child and child == node.right_child:
            self._left_rotate(parent)
        #  Zig-Zag case. Make one left turn and one right.
        elif node == parent.left_child and child == node.right_child:
            self._left_rotate(node)
            self._right_rotate(parent)
        #  Zag-Zig case. Make one right turn and one left.
        elif node == parent.right_child and child == node.left_child:
            self._right_rotate(node)
            self._left_rotate(parent)


# if __name__ == '__main__':
