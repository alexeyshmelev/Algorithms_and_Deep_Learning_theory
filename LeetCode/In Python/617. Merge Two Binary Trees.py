# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root2 == None:
            return root1
        if root1 == None:
            return root2
        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            node1.val, node2.val = node1.val+node2.val, node1.val+node2.val
            if node1.right and node2.right != None:
                stack1.append(node1.right)
                stack2.append(node2.right)
            if node1.left and node2.left != None:
                stack1.append(node1.left)
                stack2.append(node2.left)
            if node1.left == None and node2.left != None:
                node1.left = node2.left
            if node1.left != None and node2.left == None:
                node2.left = node1.left
            if node1.right == None and node2.right != None:
                node1.right = node2.right
            if node1.right != None and node2.right == None:
                node2.right = node1.right
        return root2