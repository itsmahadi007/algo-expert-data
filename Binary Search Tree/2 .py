# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        if self is None:
            self.value = value
            return self
        if value > self.value:
            self.left = self.insert(value)
        else:
            self.right = self.insert(value)

        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)
