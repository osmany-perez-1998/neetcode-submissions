# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        low,high = (p,q) if p.val <= q.val else (q,p)
         

        while(True):
            if low.val <= ancestor.val and ancestor.val <= high.val:
                return ancestor
            if max(low.val, high.val) < ancestor.val:
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right