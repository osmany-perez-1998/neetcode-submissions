# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = [p]
        queue2 = [q]

        def are_two_nodes_eq(p,q):
            if (not p and not q): return True
            
            if (not p or not q) or  (p.val - q.val): return False

            return True

            
            

        while queue1:
            father1 = queue1.pop(0)
            father2 = queue2.pop(0)

            if not are_two_nodes_eq(father1,father2):
                return False            
            
            if not father1 and not father2:
                continue

            queue1.append(father1.left)
            queue2.append(father2.left)            
            
            queue1.append(father1.right)
            queue2.append(father2.right)
        
        return True


        