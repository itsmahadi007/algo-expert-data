class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data if data else None
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root


def search(root, value):
    # node is empty
    if root is None:
        return False
    # if element is equal to the element to be searched
    elif root.data == value:
        return True
    # element to be searched is less than the current node
    elif root.data > value:
        return search(root.leftChild, value)
    # element to be searched is greater than the current node
    else:
        return search(root.rightChild, value)


def inorder(self):
    if self is not None:
        inorder(self.leftChild)
        print(self.data, end=" ")
        inorder(self.rightChild)


def minValueNode(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current


def delete(root, value):
    if root is None:
        return root
    if value < root.data:
        root.leftChild = delete(root.leftChild, value)
    elif value > root.data:
        root.rightChild = delete(root.rightChild, value)
    else:
        # if node to be deleted has no children
        if root.leftChild is None and root.rightChild is None:
            root = None
        # if node to be deleted has only one child
        elif root.leftChild is None:
            temp = root
            root = root.rightChild
            temp = None
        elif root.rightChild is None:
            temp = root
            root = root.leftChild
            temp = None
        # if node to be deleted has two children
        else:
            temp = minValueNode(root.rightChild)
            root.data = temp.data
            root.rightChild = delete(root.rightChild, temp.data)
    return root


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)

print("53 is present in the binary tree:", search(root, 53))
print("100 is present in the binary tree:", search(root, 100))
inorder(root)
