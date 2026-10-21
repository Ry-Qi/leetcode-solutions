# No. 143 Reorder List
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        # 1 2 3 4 5
        # 1 2
        # 5 4 3

        # 1 2 3 4
        # 1 2
        # 4 3
        # 1 4 2 3
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev:
            return head
        prev.next = None
        l1, l2 = head, slow
        prev, cur, nxt = None, l2, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        l2 = prev
        res = tail = ListNode(-1)
        while l1 or l2:
            if l1:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            if l2:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        # No need
        # head = res
