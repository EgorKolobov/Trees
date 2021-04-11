from BaseTree import BaseTree, Node


class SplayTree(BaseTree):
    def __init__(self, root: Node = None):
        super().__init__(root)

    # 'splays' the tree. helps most recent used Node be the root of the tree
    def _splay(self, some_node: Node) -> None:
        if some_node is None:
            return
        while some_node.parent is not None:
            # Zig case. Make one turn.
            if some_node.parent == self.root:
                if some_node == some_node.parent.left_child:
                    self._right_rotate(some_node.parent)
                else:
                    self._left_rotate(some_node.parent)
            else:
                # Left Zig-Zig case. Make two right turns.
                if some_node == some_node.parent.left_child and some_node.parent == some_node.parent.parent.left_child:
                    self._right_rotate(some_node.parent.parent)
                    self._right_rotate(some_node.parent)
                # Right Zig-Zig case. Make two left turns.
                elif some_node == some_node.parent.right_child and some_node.parent == some_node.parent.parent.right_child:
                    self._left_rotate(some_node.parent.parent)
                    self._left_rotate(some_node.parent)
                # Left-Right Zig-Zag case '<'. Make one left turn and one right.
                elif some_node == some_node.parent.right_child and some_node.parent == some_node.parent.parent.left_child:
                    self._left_rotate(some_node.parent)
                    self._right_rotate(some_node.parent)
                # Right-Left Zig-Zag case '>'. Make one right turn and one left.
                elif some_node == some_node.parent.left_child and some_node.parent == some_node.parent.parent.right_child:
                    self._right_rotate(some_node.parent)
                    self._left_rotate(some_node.parent)

    # performs a search in a whole tree. returns Node if found else None
    def search_node(self, search_value) -> Node:
        result_node = super().search_node(search_value)
        self._splay(result_node)
        return result_node

    # inserts a new node with needed value to the tree
    def insert(self, value) -> None:
        self._splay(super().insert(value))

    # removes Node from the tree
    def remove(self, value) -> None:
        remove_node = self.search_node(value)
        if remove_node is not None:
            if remove_node.left_child is None:
                self._place_child_to_parent(remove_node, remove_node.right_child)
            elif remove_node.right_child is None:
                self._place_child_to_parent(remove_node, remove_node.left_child)
            else:
                replacer = self.min_node(remove_node.right_child)
                if replacer.parent != remove_node:
                    self._place_child_to_parent(replacer, replacer.right_child)
                    replacer.right_child = remove_node.right_child
                    replacer.right_child.parent = replacer
                self._place_child_to_parent(remove_node, replacer)
                replacer.left_child = remove_node.left_child
                replacer.left_child.parent = replacer

                self._splay(replacer)

            del remove_node


# if __name__ == '__main__':
