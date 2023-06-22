from typing import Optional

from DataStructures import *


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempNode = head
        for i in range(k):

            while tempNode.next.next:
                tempNode = tempNode.next

            tempNode.next.next = head
            head = tempNode.next
            tempNode.next = None
        return head
