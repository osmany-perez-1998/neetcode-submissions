# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        aux1 = root.right        
        
        root.right = self.invertTree(root.left) if root.left else None
        root.left =  self.invertTree(aux1) if aux1 else None

        return root
        