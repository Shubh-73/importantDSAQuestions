import sys
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


height = 0
maximumHeight = -12324
maxSum = 0

def deepestLeaves(root: Optional[TreeNode]) -> int:
    global maxSum
    inorder(root, height)
    return maxSum


def inorder(root, height):
    global maximumHeight
    global maxSum

    if root is None:
        return

    height += 1
    inorder(root.left, height)
    if root.left is None and root.right is None:
        if maximumHeight < height:
            maximumHeight = height
            maxSum = root.val
        elif maximumHeight == height:
            maxSum += root.val

    inorder(root.right, height)

def printTree(root: Optional[TreeNode]) -> None:
    if root is None:
        return
    list = []
    list.append(root)
    while len(list) > 0:
        size = len(list)
        for i in range(size):
            currentNode = list.pop(0)
            print(currentNode.val, end=" ")

            if currentNode.left is not None:
                list.append(currentNode.left)

            if currentNode.right is not None:
                list.append(currentNode.right)
        print(" ")


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    printTree(root)
    print(deepestLeaves(root))
