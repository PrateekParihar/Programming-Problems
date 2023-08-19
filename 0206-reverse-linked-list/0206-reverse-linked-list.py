# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        p1, p2 = None, head
        
        while p2.next is not None:
            
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
            
        p2.next = p1
        
        return p2
            
            