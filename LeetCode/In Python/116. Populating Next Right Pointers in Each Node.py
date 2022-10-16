"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        queue = [root]
        i = 0
        l = 2 ** i

        while queue:
            node = queue.pop(0)

            if p := node.left:
                queue.append(p)
            if p := node.right:
                queue.append(p)

            l -= 1
            if l == 0:
                i += 1
                l = 2 ** i
            else:
                node.next = queue[0]

        return root
