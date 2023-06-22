from typing import Optional

from DataStructures import *


def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def searchLink(fast_ptr_node, slow_ptr_node):
    if not fast_ptr_node and not fast_ptr_node.next:
        return False
    if fast_ptr_node is fast_ptr_node.next:
        return True
    try:
        searchLink(fast_ptr_node.next.next, slow_ptr_node.next)
    except:
        return False
