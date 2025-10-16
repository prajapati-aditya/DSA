# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")

        def dfs(node) :
            if not node : return 0

            left_path = max(0,dfs(node.left))
            right_path = max(0,dfs(node.right))
            # update max_path_sum
            self.max_path = max(self.max_path, left_path+right_path+node.val)
            # return the max one path val
            return max(left_path,right_path)+node.val
        dfs(root)
        return self.max_path
        