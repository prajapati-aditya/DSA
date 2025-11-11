# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen_nodes = {}
        sets =set()     # contains nodes that has parents

        for parent,child,lr in descriptions :
            if parent not in seen_nodes :
                seen_nodes[parent] = TreeNode(parent)
                
            
            if child not in seen_nodes :
                    seen_nodes[child] = TreeNode(child)
                
            if lr ==1 :     # left child
                seen_nodes[parent].left = seen_nodes[child]
                
            else :          # right child
                seen_nodes[parent].right = seen_nodes[child]
            sets.add(child)
                
        for parent,child,lr in descriptions :
            if parent not in sets:
                return seen_nodes[parent]
        
        