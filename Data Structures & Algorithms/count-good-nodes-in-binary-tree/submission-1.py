# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, root.val)]
        ans = 1

        while stack:
            aux, _max = stack.pop()

            if aux.left:
                stack.append((aux.left,max(_max, aux.left.val)))
                if _max <= aux.left.val:
                    ans+=1
                    
            if aux.right:
                stack.append((aux.right,max(_max, aux.right.val)))
                if _max <= aux.right.val:
                    ans+=1

        return ans
            




        