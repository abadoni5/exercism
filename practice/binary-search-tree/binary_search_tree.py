"""
Approach:
- The provided code defines two classes: TreeNode and BinarySearchTree.
- TreeNode represents a single node in a binary search tree, while BinarySearchTree represents the binary search tree itself.
- TreeNode contains the data stored in the node and references to its left and right child nodes.
- BinarySearchTree initializes with a list of data elements and inserts each element into the binary search tree.
- Insertion is done recursively by comparing the data with each node and traversing either the left or right subtree accordingly.
- The search method recursively searches for a specific data element in the binary search tree.
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.insert(data)

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def data(self):
        return self.root

    def sorted_data(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [node.data] + self._inorder_traversal(node.right)
