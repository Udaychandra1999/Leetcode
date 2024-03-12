# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        l=[]
        
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        flag =True
        while(flag):
            n = len(l)
            c=0
            for i in range(n):
                for j in range(i+1,n+1):
                    if sum(l[i:j])==0:
                        c+=1
                        del l[i:j]
            if c == 0:
                flag = False
        print(l)
        ptr = head2 = ListNode(0)
        for e in l:
            if e!=0:
                ptr.next = ListNode(e)
                ptr = ptr.next

        return head2.next
