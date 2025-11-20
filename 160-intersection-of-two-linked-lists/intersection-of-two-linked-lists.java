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
    public int getLength(ListNode root){
        int s = 0;
        ListNode ptr = root;
        while(root!= null){
            root = root.next;
            s++;
        }
        return s;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int a=0,b=0;
        ListNode pa = headA;
        ListNode pb = headB;
        a = getLength(headA);
        b = getLength(headB);
        int diffa=0,diffb=0;
        if (a>b){
            diffa = a-b;
        }else {
            diffb = b-a;
        }
        while (diffa>0){
            pa = pa.next;
            diffa--;
        }
        while(diffb>0){
            pb = pb.next;
            diffb--;
        }
        while(pa!= null && pb!=null){
            if (pa == pb){
                return pa;
            }
            pa = pa.next;
            pb = pb.next;
        }
        return null;
    }
}