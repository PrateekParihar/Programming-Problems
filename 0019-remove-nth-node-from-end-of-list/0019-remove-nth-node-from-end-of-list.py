# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """        *   ^
          H->D,1,2,3,4,5 -> Null
        
        p1 -> head
        p2 -> p1 + n 
        
        nth node from the end of the list -> p1+1
        while p2.next == null
        remove -> p1.next.next = null -> p1.next = p2
            * ^      
          D,1,2 -> None
        
        """
        dummy = ListNode()
        dummy.next = head
        
        p1 = dummy
        p2 = p1
        for i in range(n):
            p2 = p2.next
            
        while p2 and p2.next != None:
            p2=p2.next
            p1=p1.next
        

        p1.next= p1.next.next

        return dummy.next
            