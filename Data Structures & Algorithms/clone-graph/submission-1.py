"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        node_dict = {}
        # node_main = {node.val: False}
        stack = [node]

        while stack:
            el = stack.pop()
            _nod = node_dict.get(el.val,None)
            if _nod and _nod.neighbors:
                continue

            stack.extend(el.neighbors)
            if el.val not in node_dict:
                node_dict[el.val] = Node (el.val)
            # node_main[el.val] = True
            
            
            for n in el.neighbors:
                if n.val not in node_dict:
                    node_dict[n.val] = Node(n.val) 

                node_dict[el.val].neighbors.append(node_dict[n.val])

        return node_dict[node.val]