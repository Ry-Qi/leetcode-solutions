# No.25
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from collections import defaultdict
from concurrent.futures import thread


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def reverse(head):
    if not head or not head.next:
        return head
    prev, cur, next = None, head, head.next
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def reverseKGroup(head, k):
    head = reverse(head)
    tail = dummy = ListNode(0, head)
    cur = head
    while cur:
        groupTail = groupHead = cur
        end = False
        for _ in range(k-1):
            groupTail = groupTail.next
            if not groupTail:
                end = True
                tail.next = cur
                break
        if end: break
        nextGroup = groupTail.next
        prev, cur, next = groupTail, groupHead, None
        while cur != nextGroup:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        tail.next = groupTail
        groupHead.next = None
        tail = groupHead
    return reverse(dummy.next)

Tail = Head = ListNode(0, None)

def Print(Head):
    cur = Head
    while cur:
        print(cur.val,end=' ')
        cur = cur.next
    print()

for i in range(1, 4):
    Tail.next = ListNode(i, None)
    Tail = Tail.next

Print(reverseKGroup(Head, 3))

# 0 1 2 3 4 5 6 7 8 9 10









