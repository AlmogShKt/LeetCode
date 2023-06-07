# Definition for singly-linked list.
from typing import Optional
from DataStructures import ListNode



def print_list(node):
    current = node
    while current is not None:
        print(current.val)
        current = current.next


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


# Create a list with values 1, 2, 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link the nodes together
node1.next = node2
node2.next = node3

# Create a list with values 1, 2, 3
node11 = ListNode(1)
node22 = ListNode(5)
node33 = ListNode(6)

# Link the nodes together
node11.next = node22
node22.next = node33

# Resulting list: 1 -> 2 -> 3

print_list(mergeTwoLists(node11, node1))
