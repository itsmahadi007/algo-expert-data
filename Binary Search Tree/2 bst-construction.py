# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
import networkx as nx
import matplotlib.pyplot as plt


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
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

        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
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

    def visualize(self):
        graph = nx.DiGraph()
        positions = {}
        levels = {}

        def traverse(node, x=0, y=0, layer=0):
            if node:
                graph.add_node(node.value, pos=(x, y))
                if node.left:
                    graph.add_edge(node.value, node.left.value)
                    l = traverse(
                        node.left,
                        x=x - 1 / (2 ** (layer + 1)),
                        y=y - 1,
                        layer=layer + 1,
                    )
                if node.right:
                    graph.add_edge(node.value, node.right.value)
                    r = traverse(
                        node.right,
                        x=x + 1 / (2 ** (layer + 1)),
                        y=y - 1,
                        layer=layer + 1,
                    )

        traverse(self)

        pos = nx.get_node_attributes(graph, "pos")
        nx.draw(
            graph,
            pos,
            with_labels=True,
            arrows=True,
            node_size=5000,
            node_color="skyblue",
        )

        plt.title("BST Visualization")
        plt.show()


root = BST(10)
# root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
# root.left.right = BST(5)
# root.right = BST(15)
# root.right.left = BST(13)
# root.right.left.right = BST(14)
# root.right.right = BST(22)

root.insert(12)

root.printTree()
# root.visualize()
