# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            def find_h (root) :
                if not root : return 0

                # find left height 
                left_h = find_h(root.left)
                if left_h == -1 : return -1

                # find right height
                right_h = find_h(root.right)
                if right_h == -1 :
                    return -1

                # find diff between left and right height
                if abs(left_h -  right_h) > 1:
                    return -1
                return 1+max(left_h , right_h)

            return find_h(root) != -1


























 
        