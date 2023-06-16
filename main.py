from typing import Optional

from DataStructures import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    cur = root
    if not cur:
        return 0

    left_dep = maxDepth(root.left) + 1
    right_dep = maxDepth(root.right) + 1
    return max(right_dep,left_dep)



