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
        stack = [node]
        aux_node = Node(0)

        while stack:
            el = stack.pop()
            
            if node_dict.get(el.val,aux_node).neighbors:
                continue

            # stack.extend(el.neighbors)
            if el.val not in node_dict:
                node_dict[el.val] = Node (el.val)
            
            
            for n in el.neighbors:
                if n.val not in node_dict:
                    node_dict[n.val] = Node(n.val) 
                    stack.append(n)

                node_dict[el.val].neighbors.append(node_dict[n.val])

        return node_dict[node.val]