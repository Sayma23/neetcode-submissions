# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return head
        sec = ListNode(head.val, None)
        temp = head
        while temp.next != None:
            third = ListNode(temp.next.val)
            third.next = sec
            sec = third
            temp = temp.next
        return sec
