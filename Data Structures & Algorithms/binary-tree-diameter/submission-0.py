# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], ) -> int:
        _max = [0]
        a= self.diameterOfBinaryTreeAux(root,_max)

        return max(a - 1,_max[0])


    
    def diameterOfBinaryTreeAux(self, root: Optional[TreeNode], _max : List) -> int:

        if not root:
            return 0      

        depth1 = self.diameterOfBinaryTreeAux(root.left, _max)
        depth2 = self.diameterOfBinaryTreeAux(root.right,_max)

        diameter = depth1 + depth2

        _max[0] = max(_max[0], diameter)

        return 1 + max (depth1, depth2)

        
    

        