# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def find_node(root: Optional[TreeNode], subRoot:Optional[TreeNode]) -> List[Optional[TreeNode]]:           
            nodes = []
            stack = [root]

            while stack:
                aux = stack.pop()
                if not aux:
                    continue
                if aux.val == subRoot.val:
                    nodes.append(aux)

                stack.append(aux.left)
                stack.append(aux.right)            
            return nodes

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        val_nodes = find_node(root, subRoot)     

        for val_node in val_nodes:            
            stack = [val_node]
            stack2 = [subRoot]
            
            while stack:
                aux = stack.pop()
                aux2 = stack2.pop()

                if not aux and not aux2:
                    continue
                elif not aux or not aux2:
                    break

                if aux.val != aux2.val:
                    break
                else:
                    stack.append(aux.left)
                    stack.append(aux.right)  

                    stack2.append(aux2.left)
                    stack2.append(aux2.right)  
            else:
                return True
        
        return False

        