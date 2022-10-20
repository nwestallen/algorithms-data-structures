class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def inorder_op(root: TreeNode, func):
    if root:
        inorder_op(root.left, func)
        func(root.val)
        inorder_op(root.right, func)

def preorder_op(root: TreeNode, func):
    if root:
        func(root.val)
        preorder_op(root.left, func)
        preorder_op(root.right, func)

def postorder_op(root: TreeNode, func):
    if root:
        postorder_op(root.left, func)
        postorder_op(root.right, func)
        func(root.val)

tree_1 = TreeNode(1)
tree_3 = TreeNode(3)
tree_5 = TreeNode(5)
tree_7 = TreeNode(7)
tree_2 = TreeNode(2, tree_1, tree_3)
tree_6 = TreeNode(6, tree_5, tree_7)
tree_4 = TreeNode(4, tree_2, tree_6)

def test_inorder():
    inorder_list = []
    inorder_op(tree_4, inorder_list.append)
    assert inorder_list == [1, 2, 3, 4, 5, 6, 7]

def test_preorder():
    preorder_list = []
    preorder_op(tree_4, preorder_list.append)
    assert preorder_list == [4, 2, 1, 3, 6, 5, 7]

def test_postorder():
    postorder_list = []
    postorder_op(tree_4, postorder_list.append)
    assert postorder_list == [1, 3, 2, 5, 7, 6, 4]
