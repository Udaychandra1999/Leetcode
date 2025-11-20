/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> li = new HashSet<>();
        ListNode a = headA;
        while (a!=null){
            li.add(a);
            a = a.next;
        }
        ListNode b = headB;
        while(b!=null){
            if(li.contains(b)){
                return b;
            }
            li.add(b);
            b=b.next;
        }
        return null;
    }
}