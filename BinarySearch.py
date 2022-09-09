class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree_data = tree_data
        self.root = None

    def data(self, value):
        if not self.root:
            self.root = TreeNode(value)

        for index in range(len(self.tree_data)):
            if len(self.tree_data) == 1:
                self.insert(None, self.tree_data)
            else:
                self.insert(self.tree_data[index], self.tree_data[index+1])

        # for index in range(len(self.tree_data)):
        #     if len(self.tree_data) == 1:
        #         tree_node = TreeNode(self.root)
        #         return tree_node
        #     if self.tree_data[index] >= self.tree_data[index+1]:
        #         tree_node = TreeNode(self.tree_data[index], TreeNode(self.tree_data[index+1]))
        #     if self.tree_data[index] < self.tree_data[index + 1]:
        #         tree_node = TreeNode(self.tree_data[index], None, TreeNode(self.tree_data[index + 1]))
        #     return tree_node

    def insert(self, value):
        if not self.root:
            root = TreeNode(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def sorted_data(self):
        pass


if __name__ == "__main__":
    print(BinarySearchTree(["4", "2", "6"]).data())
