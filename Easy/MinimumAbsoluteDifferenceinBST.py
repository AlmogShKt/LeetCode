import sys
from DataStructures import TreeNode

def getMinimumDifference(root) -> int:
    values_list = serach(root, [])
    diff = sys.maxsize

    for i in range(1, len(values_list)):
        diff = min(diff, values_list[i] - values_list[i - 1])

    return diff


def serach(tree, tree_values):
    if not tree:
        return

    serach(tree.left, tree_values)
    tree_values.append(tree.val)
    serach(tree.right, tree_values)

    return tree_values

