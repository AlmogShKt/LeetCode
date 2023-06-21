def invertTree(root):

    def rec(root):
        if not root:
            return
        if root.left and root.right:
            tempNode = root.right
            root.right = root.left
            root.left = tempNode
        rec(root.left)
        rec(root.right)

        return root

    return rec(root)
