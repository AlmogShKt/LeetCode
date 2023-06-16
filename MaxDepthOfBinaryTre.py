# 104. Maximum Depth of Binary Tree
from typing import Optional

from DataStructures import *
def maxDepth(root: Optional[TreeNode]) -> int:
    cur = root
    if not cur:
        return 0

    left_dep = maxDepth(root.left) + 1
    right_dep = maxDepth(root.right) + 1
    return max(right_dep,left_dep)



