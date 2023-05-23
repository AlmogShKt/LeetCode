# 23-5-23

from typing import Optional
from DataTypes import ListNode

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_list = tail = ListNode()
    temp_list1 = list1
    temp_list2 = list2

    while temp_list1 and temp_list2:
        if temp_list1.val >= temp_list2.val:
            tail.next = temp_list2
            temp_list2 = temp_list2.next
        else:
            tail.next = temp_list1
            temp_list1 = temp_list1.next
        tail = tail.next

    if temp_list1:
        tail.next = temp_list1
    else:
        tail.next = temp_list2

    return merged_list.next