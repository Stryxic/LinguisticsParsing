import node, link
from collections import deque

class Tree:
    def __init__(self, node_1:node.Node, node_2:node.Node, link:link.Link, id) -> None:
        self.id = id
        self.nodes = {node_1.id:node_1, node_2.id:node_2}
        self.links = [link]

    def get_nodes(self):
        return self.nodes
    
    def get_links(self):
        return self.links

    def add_node(self, node):
        self.nodes[node.id] = node

    def remove_node(self, id):
        if id in self.nodes:
            del(self.nodes[id])

    def add_link(self, link):
        if link.end and link.end.id not in self.nodes:
            self.add_node(link.end)
        self.links.append(link)

    def add_node_link(self, id, link):
        if id in self.nodes:
            self.nodes[id].add_link(link)
            

    def remove_link(self, id):
        self.links = [link for link in self.links if link.id != id]

    def __str__(self) -> str:
        return "\n".join(str(link) for link in self.links)
    
    def traverse_tree(self, tranversal_type="dfs"):
        if tranversal_type == "dfs":
            return self._dfs()
        elif tranversal_type == "bfs":
            return self._bfs()
        
        else:
            raise ValueError("Unsupported traversal type.")
        
    
    def _dfs(self):
        visited = set()
        result = []

        def dfs(node:node.Node):
            if node.id in visited:
                return
            visited.add(node.id)
            result.append(node)
            for link in node.links:
                if link.end:
                    dfs(link.end)

        if self.nodes:
            start_node = self.nodes[next(iter(self.nodes))]
            dfs(start_node)
        return result
    

    def _bfs(self):
        visited = set()
        queue = deque()
        result = []

        if self.nodes:
            start_node = self.nodes[next(iter(self.nodes))]
            queue.append(start_node)
            visited.add(start_node.id)


        while queue:
            current = queue.popleft()
            result.append(current)
            for link in current.links:
                if link.end and link.end.id not in visited:
                    queue.append(link.end)
                    visited.add(link.end.id)

        return result

