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
        
        ListNode H = head;
        
        while(H != null && H.next != null){
            T = T.next;
            H = H.next.next;
            
            if (T == H){
                return true;
            }
        }
        
        return false;

    }
}