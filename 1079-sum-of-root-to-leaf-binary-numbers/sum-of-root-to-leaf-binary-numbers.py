# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node,binary) :
            if not node : return 

            binary += str(node.val)

            if not node.left and not node.right :
                self.res += int(binary,2)
                return
            dfs(node.left,binary)
            dfs(node.right,binary)
        dfs(root,"")
        return self.res
        