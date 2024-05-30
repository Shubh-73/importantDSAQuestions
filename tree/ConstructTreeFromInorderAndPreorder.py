
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):

        return self.helperFunction(preorder, 0, len(preorder) - 1, inorder,
                                   0, len(inorder) - 1)



    def helperFunction(self, preorder, preorder_start_idx, preorder_end_idx, inorder,
                       inorder_start_idx, inorder_end_idx):


        if inorder_start_idx > inorder_end_idx or preorder_start_idx > preorder_end_idx:
            return None

        root = TreeNode(preorder[preorder_start_idx])
        rootIndexInInorder  = inorder_start_idx
        while root.val != inorder[rootIndexInInorder]:
            rootIndexInInorder += 1

        left_sub_tree_size = preorder_start_idx + rootIndexInInorder

        root.left = self.helperFunction(preorder, preorder_start_idx + 1, preorder_start_idx + left_sub_tree_size,
                                   inorder, inorder_start_idx, rootIndexInInorder -1)

        root.right = self.helperFunction(preorder, preorder_start_idx + left_sub_tree_size + 1, preorder_end_idx,
                                         inorder, rootIndexInInorder + 1, inorder_end_idx)

        return root

def print_tree(node, depth=0):
    if not node:
        return
    print_tree(node.right, depth + 1)
    print(" " * 4 * depth + "->", node.val)
    print_tree(node.left, depth + 1)

def main():
    print("Starting main function...")  # Debug statement
    inorder = [6,4,7,2,1,10,3,8,5,9]
    preorder = [1,2,4,6,7,3,10,5,8,9]

    solution = Solution()
    print("Building tree...")  # Debug statement
    root = solution.buildTree(preorder, inorder)

    if root is None:
        print("Tree is empty.")  # Debug statement
    else:
        print("Tree built. Printing tree:")  # Debug statement
        # Function to print the tree
        print_tree(root)
        print("Tree printing complete.")  # Debug statement

if __name__ == "__main__":
    main()