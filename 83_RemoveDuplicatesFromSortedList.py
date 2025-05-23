# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while p1:
            if p1.next:
                p2 = p1.next
            
            while p2 and p2.val == p1.val:
                if p2.next:
                    p2 = p2.next
                else:
                    p2 = None
            
            p1.next = p2
            p1 = p2

        return head