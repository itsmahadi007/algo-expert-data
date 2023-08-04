def findClosestValueInBst(tree, target, closest=None):
    if tree is None:
        return closest
    print(tree.value, closest, target)
    # Update closest if the current node is closer to the target
    if closest is None or abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    # Decide which way to go
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print("23 closest in the binary tree:", findClosestValueInBst(root, 23))
