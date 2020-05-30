class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        self.root = TreeNode(val)
    
    def preorder_print(self):
        def recursion(node):
            if not node:
                return
            print(node.val)
            recursion(node.left)
            recursion(node.right)

        recursion(self.root)

    def inorder_print(self):
        def recursion(node):
            if not node:
                return
            recursion(node.left)
            print(node.val)
            recursion(node.right)
    
        recursion(self.root)
mytree = Tree(1)
mytree.root.left = TreeNode(2)
mytree.root.left.left = TreeNode(11)
mytree.root.left.right = TreeNode(4)
mytree.root.right = TreeNode(5)
mytree.root.right.left = TreeNode(7)
mytree.root.right.right = TreeNode(8)

mytree.preorder_print()
mytree.inorder_print()