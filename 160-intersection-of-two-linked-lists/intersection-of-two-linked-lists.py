# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        s = set()
        while a:
            if a not in s:
                s.add(a)
            a = a.next
        b = headB
        while b:
            if b not in s:
                s.add(b)
            else:
                return b
            b = b.next
