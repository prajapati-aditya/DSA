# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [ ]

        if not root :
            return res
        nodeQue  = deque()
        nodeQue.append(root)
        LtoR = True
        while nodeQue :
            size = len(nodeQue)
            row =[0]*size
            for i in range(size) :
                node = nodeQue.popleft()
                index = i if LtoR else(size-1-i)
                row[index] = node.val
                if node.left :
                    nodeQue.append(node.left)
                if node.right :
                    nodeQue.append(node.right)
            LtoR = not LtoR
            res.append(row)
        return res
        