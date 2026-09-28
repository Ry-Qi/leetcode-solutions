# No.24 Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs1(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        nxtgrp = head
        dummy = tail = ListNode(0, head)
        # 1 2 n
        first = second = None

        while nxtgrp:
            first, second = nxtgrp, nxtgrp.next
            if not second:
                tail.next = first
                break
            nxtgrp = second.next
            second.next = first
            first.next = None
            tail.next = second
            tail = first

        return dummy.next

    def swapPairs2(self, head):
        if not head or not head.next:
            return head
        first, second = head, head.next
        nxtgrp = second.next
        second.next = first
        first.next = self.swapPairs2(nxtgrp)
        return second


