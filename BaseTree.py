# Node/vertex of a binary tree
class Node():
    def __init__(self, value=None, parent=None, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent


class BaseTree():  # Describes a basic binary search tree
    def __init__(self, root: Node = None):
        self.root = root

    # disconects child and some_parent and attaches child to some_parent.parent
    def _place_child_to_parent(self, some_parent: Node, child: Node) -> None:
        if some_parent.parent is None:
            self.root = child
        elif some_parent == some_parent.parent.left_child:
            some_parent.parent.left_child = child
        elif some_parent == some_parent.parent.right_child:
            some_parent.parent.right_child = child
        if child is not None:
            child.parent = some_parent.parent

    # make left rotation for some_node
    def _left_rotate(self, some_node: Node) -> None:
        Rchild = some_node.right_child
        if Rchild is None:
            return
        else:
            some_node.right_child = Rchild.left_child
        if Rchild.left_child is not None:
            Rchild.left_child.parent = some_node
        self._place_child_to_parent(some_node, Rchild)
        Rchild.left_child = some_node
        Rchild.left_child.parent = Rchild

    # make right rotation for some_node
    def _right_rotate(self, some_node: Node) -> None:
        Lchild = some_node.left_child
        if Lchild is None:
            return
        else:
            some_node.left_child = Lchild.right_child
        if Lchild.right_child is not None:
            Lchild.right_child.parent = some_node
        self._place_child_to_parent(some_node, Lchild)
        Lchild.right_child = some_node
        Lchild.right_child.parent = Lchild

    # returns a Node with minimum value in a subtree(root=some_node)
    def min_node(self, some_node: Node = None) -> Node:
        if some_node is None:
            min_node = self.root
        else:
            min_node = some_node
        while min_node.left_child is not None:
            min_node = min_node.left_child
        return min_node

    # returns a Node with maximum value in a subtree(root=some_node)
    def max_node(self, some_node: Node = None) -> Node:
        if some_node is None:
            max_node = self.root
        else:
            max_node = some_node
        while max_node.right_child is not None:
            max_node = max_node.right_child
        return max_node

    # inserts a new node with needed value to the tree. returns new Node
    def insert(self, value) -> Node:
        parent_for_new_node = None
        place_for_newnode = self.root

        while place_for_newnode is not None:
            parent_for_new_node = place_for_newnode
            if value >= place_for_newnode.value:
                place_for_newnode = place_for_newnode.right_child
            elif value < place_for_newnode.value:
                place_for_newnode = place_for_newnode.left_child

        new_node = Node(value, parent_for_new_node)
        if parent_for_new_node is None:
            self.root = new_node
        elif new_node.value >= parent_for_new_node.value:
            parent_for_new_node.right_child = new_node
        elif new_node.value < parent_for_new_node.value:
            parent_for_new_node.left_child = new_node
        return new_node

    # performs a search in a whole tree. returns Node if found else None
    def search_node(self, search_value) -> Node:
        result_node = self.root
        while result_node is not None:
            if search_value > result_node.value:
                result_node = result_node.right_child
            elif search_value < result_node.value:
                result_node = result_node.left_child
            elif search_value == result_node.value:
                return result_node
