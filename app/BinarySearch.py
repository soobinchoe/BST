class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        self.value = tree_data

    def data(self):
        if not self.root:
            self.root = TreeNode(self.value[0])

        if len(self.value) > 1:
            self._data(self.value, self.root)

        return self.root

    def _data(self, value, current_node):
        for i in range(len(value)):
            if value[i] < current_node.data:
                if not current_node.left:
                    current_node.left = TreeNode(value[i])
                else:
                    self._data(value[i], current_node)
            elif value[i] > current_node.data:
                if not current_node.right:
                    current_node.right = TreeNode(value[i])
                else:
                    self._data(value[i], current_node.right)

    def sorted_data(self):
        pass


if __name__ == "__main__":
    print(BinarySearchTree(["4", "2"]).data())
