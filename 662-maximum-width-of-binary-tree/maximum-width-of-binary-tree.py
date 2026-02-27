
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])
        
        while queue:
            size = len(queue)
            first_index = queue[0][1]
            
            for i in range(size):
                node, index = queue.popleft()
                
                # normalize index at every level
                index -= first_index
                
                if i == size - 1:       # last index of the level
                    max_width = max(max_width, index + 1)
                
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width