/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        ListNode T = head;
        
        ListNode H = T;
        
        while(H != null && T != null){
            

            if(H.next == null || T.next == null){
                return false;
            }
                        T = T.next;
            H = H.next.next;
            
            if (H == T){
                return true;
            }
        }
        
        return false;
    }
}