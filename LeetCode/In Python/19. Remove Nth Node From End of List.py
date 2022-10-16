# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i, l, r, s = 0, head, head, head
        while head is not None:
            if i > n:
                l = l.next
            if i > n - 2:
                r = r.next
            i += 1
            head = head.next
        if n == i:
            return s.next
        else:
            l.next = r
            return s
