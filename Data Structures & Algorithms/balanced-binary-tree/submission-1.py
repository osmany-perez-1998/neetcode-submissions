# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        _balanced = [True]
        a= self.diameterOfBinaryTreeAux(root,_balanced)

        return _balanced[0]


    #Copied code: it should be height of binary tree
    def diameterOfBinaryTreeAux(self, root: Optional[TreeNode], _max : List) -> int:

        if not root:
            return 0      

        depth1 = self.diameterOfBinaryTreeAux(root.left, _max)
        depth2 = self.diameterOfBinaryTreeAux(root.right,_max)

        if -1<= (depth1-depth2)<= 1:
            pass
        else:
            _max[0] = False

        return 1 + max (depth1, depth2)