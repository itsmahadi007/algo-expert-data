class BST:
    def __init__(self, data=None):
        self.data = data if data else None
        self.left = None
        self.right = None


def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        # print("root is none", newValue)
        root = BST(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        # print(root.left, newValue, "left")
        root.left = insert(root.left, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        # print(root.left, newValue, "left")
        root.right = insert(root.right, newValue)
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
        return search(root.left, value)
    # element to be searched is greater than the current node
    else:
        return search(root.right, value)


def inorder(self):
    if self is not None:
        inorder(self.left)
        print(self.data, end=" ")
        inorder(self.right)


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


def delete(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        # if node to be deleted has no children
        if root.left is None and root.right is None:
            root = None
        # if node to be deleted has only one child
        elif root.left is None:
            temp = root
            root = root.right
            temp = None
        elif root.right is None:
            temp = root
            root = root.left
            temp = None
        # if node to be deleted has two children
        else:
            temp = minValueNode(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
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
print()
print("Min Value", minValueNode(root).data, "Max Value", maxValueNode(root).data)
