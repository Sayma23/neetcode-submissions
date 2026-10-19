# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        t1 = l1
        t2 = l2
        dummy = cur = ListNode()
        while t1 and t2:
            total = t1.val + t2.val + carry
            res = ListNode(total % 10)
            carry = total // 10
            cur.next = res
            cur = cur.next
            t1, t2 = t1.next, t2.next
        while t1:
            total = t1.val + carry
            res = ListNode(total % 10)
            carry = total // 10
            cur.next = res
            cur = cur.next
            t1 = t1.next
        while t2:
            total = t2.val + carry
            res = ListNode(total % 10)
            carry = total // 10
            cur.next = res
            cur = cur.next
            t2 = t2.next
        if carry > 0:
            res = ListNode(carry)
            cur.next = res
        return dummy.next
