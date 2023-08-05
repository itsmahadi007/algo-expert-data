class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

        return self

    def contains(self, value):
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        return True

    def remove(self, value):
        if not self:
            return self
        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.right and not self.left:
                return None
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self
            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self
            else:
                successor = self.right.inOrderSuccessor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
        return self

    def inOrderSuccessor(self):
        while self.left:
            self = self.left
        return self

    def printTree(self):
        # List to store each level
        levels = []

        # Helper function to retrieve the tree level by level
        def retrieveLevels(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])
                levels[level].append(node)
                retrieveLevels(node.left, level + 1)
                retrieveLevels(node.right, level + 1)

        retrieveLevels(self, 0)

        # Printing the tree visually
        tree_height = len(levels)
        for level in range(tree_height):
            spaces = " " * (2 ** (tree_height - level) - 1)
            print(spaces, end="")
            for node in levels[level]:
                print(node.value if node else "N", end=spaces * 2)
            print()


root = BST(10)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(15)
root.insert(13)
root.insert(14)
root.insert(22)

print()
print(root.contains(22))
print()
root.printTree()
