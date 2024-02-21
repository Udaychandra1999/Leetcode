# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        p1 = l1
        p2 = l2
        i=0
        while(p1!=None):
            n1 = n1 + p1.val*(10**i)
            i+=1
            p1 = p1.next
        i=0
        while(p2!=None):
            n2 = n2 + p2.val*(10**i)
            i+=1
            p2 = p2.next
        n3 = n1+n2
        l3 = ListNode(0)
        x = n3
        ptr = l3
        if(n3 == 0):
            return l3
        while(x>0):
            ptr.next = ListNode(x%10)
            x=x//10
            ptr = ptr.next
        return l3.next
             
        