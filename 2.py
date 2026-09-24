# No.2 Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        carry = 0
        dummy = tail = ListNode()
        c1, c2 = l1, l2
        while c1 or c2 or carry!=0:
            n1 = n2 = 0
            if c1: 
                n1 = c1.val
                c1=c1.next
            if c2: 
                n2 = c2.val
                c2=c2.next
            cur = (n1+n2+carry)%10
            carry = (n1+n2+carry)//10
            tail.next = ListNode(cur)
            tail = tail.next
        
        return dummy.next


            