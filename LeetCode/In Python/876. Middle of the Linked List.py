# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        a = head
        while head is not None:
            if i % 2 != 0:
                a = a.next
            head = head.next
            i += 1
        return a