"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        dict_nodes = {node: Node(node.val)}
        queue = [node]
        while queue:
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                for neigh in curr_node.neighbors:
                    if neigh not in dict_nodes:
                        dict_nodes[neigh] = Node(neigh.val)
                        queue.append(neigh)
                    dict_nodes[curr_node].neighbors.append(dict_nodes[neigh])
                    
        return dict_nodes[node]
    
    def dfs_cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        dict_nodes = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for neigh in curr_node.neighbors:
                if neigh not in dict_nodes:
                    dict_nodes[neigh] = Node(neigh.val)
                    stack.append(neigh)
                dict_nodes[curr_node].neighbors.append(dict_nodes[neigh])
                
        return dict_nodes[node]
    
    