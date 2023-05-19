/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
//         if(head == null){
//             return head;
//         }
        
//         ListNode previous = null;
//         ListNode current;
        
//         current = head;
        
//         while(current != null){
//             ListNode tmp = current.next;
//             current.next = previous;
//             previous = current;
//             current = tmp;
//         }
        
//         return previous;
        
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;

        return newHead;
    }
}