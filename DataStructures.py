# datastructures.py

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a doubly-linked list node
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# Definition for a graph node
class GraphNode:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
