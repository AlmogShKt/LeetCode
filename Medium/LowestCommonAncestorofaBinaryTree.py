from DataStructures import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 235

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr_root = root

    while curr_root:
        if p.val > curr_root.val and q.val > curr_root.val:
            curr_root = curr_root.right
        elif p.val < curr_root.val and q.val < curr_root.val:
            curr_root = curr_root.left
        else:
            return curr_root


# 236
def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def findT(root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = findT(root.left, p, q)
        right = findT(root.right, p, q)
        if left and right:
            return root
        return left or right

    return findT(root, p, q)
