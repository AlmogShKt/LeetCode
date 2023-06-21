# 94.Binary Tree Inorder Traversal
from DataStructures import *

def inorderTraversal(root: [TreeNode]):


    def in_order(root,list):
        if not root:
            return
        in_order(root.left,list)
        list.append(root.val)
        in_order(root.right,list)
        return list

    return in_order(root,[])


