# No.19
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # get count of nodes
        total = 0
        cur = head
        while cur:
            cur=cur.next
            total+=1
        
        # get previous node of target
        cur = dummy = ListNode(0,head)
        for _ in range(total-n):
            cur = cur.next
 
        # delete it
        cur.next = cur.next.next
        return dummy.next


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class Solution2:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast = slow = dummy = ListNode(0, head)

        for _ in range(n+1):
            fast = fast.next

        # find previous node of target
        while fast:
            fast=fast.next
            slow=slow.next

        slow.next = slow.next.next

        return dummy.next
