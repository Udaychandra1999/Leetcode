# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l2 = []
        if head == None:
            return None
        ptr = head
        while(ptr != None):
            if ptr.val not in l2:
                l2.append(ptr.val)
            ptr = ptr.next
        ptr = head
        for i in range(len(l2)-1):
            ptr.val = l2[i]
            ptr= ptr.next
        ptr.val = l2[len(l2)-1]
        ptr.next = None
        return head
