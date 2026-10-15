# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while(temp):
            length += 1
            temp = temp.next
        print(length)
        pos = length - n
        temp = head
        for i in range (pos-1):
            temp = temp.next
        if(pos == 0):
            return head.next
        else:
            temp.next = temp.next.next
        return head

        