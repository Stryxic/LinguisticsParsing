import node, link
from collections import deque, defaultdict

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
    
    def tree_to_string(self):
        output_string = ""
        output_array = []
        traversal_output = self.traverse_tree()
        traversal_tree = traversal_output[0]
        depth_map = traversal_output[1]
        print(depth_map.items())
        ids_to_depths = {x[1][0].id:x[0] for x in depth_map.items()}

        link_terminals=[(x.get_start().id,x.get_end().id) for x in self.links]


        for terminals in link_terminals:
            # print(terminals[0])
            start_node_id = terminals[0]
            end_node_id = terminals[1]
            if start_node_id in ids_to_depths:
                start_node_depth = ids_to_depths[start_node_id]
            else:
                if end_node_id in ids_to_depths:
                    end_node_depth = ids_to_depths[end_node_id]
                    start_node_depth = end_node_depth - 1
            if end_node_id in ids_to_depths:
                end_node_depth = ids_to_depths[end_node_id]
            else:
                end_node_depth = start_node_depth + 1
            print(start_node_depth, end_node_depth)
            if abs(end_node_depth-start_node_depth)>1:
                if start_node_depth < end_node_depth:
                    ids_to_depths[end_node_id] = start_node_depth+1
                else:
                    ids_to_depths[start_node_id] = end_node_depth-1

        # print(link_terminals)


        # print(depths_to_ids)
        print(self.links)
        print(ids_to_depths)

        array_tree_repr = []

        max_depth = -1

        for id in ids_to_depths:
            current_depth = ids_to_depths[id]
            print(current_depth)
            # print(current_depth)
            if current_depth > max_depth:
                # print(current_depth, max_depth)
                array_tree_repr.append([id])
                max_depth = current_depth
            else:
                if current_depth < len(array_tree_repr):
                    array_tree_repr[current_depth].append(id)


        output_str = ""
        all_nodes = []
        final_nodes = []
        for element in array_tree_repr:
            current_nodes = [self.nodes[x] for x in element if x in self.nodes and self.nodes[x].content]
            node_to_children = {x.content:x.get_children() for x in current_nodes}
            contents = [x.content for x in current_nodes]
            if contents and contents != [None]:
                print(contents)
                all_nodes += contents
                final_nodes.append(current_nodes)
                # contents_to_nodes = 
                # print(node_to_children)

        #print(array_tree_repr)
        print(final_nodes)    
        print(all_nodes)
        # print(self.links)
        spanning_links = []
        for link in self.links:
            print(link)
            if link.get_start().content in all_nodes or link.get_end().content in all_nodes:
                spanning_links.append(link)
        print(spanning_links)
        return(spanning_links, final_nodes, all_nodes)
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
        depth_map = defaultdict(list)

        def dfs(node:node.Node, depth):
            if node.id in visited:
                return
            visited.add(node.id)
            result.append(node)
            depth_map[depth].append(node)
            for link in node.links:
                if link.end:
                    dfs(link.end, depth+1)

        if self.nodes:
            start_node = self.nodes[next(iter(self.nodes))]
            dfs(start_node, 0)
        return [result, depth_map]
    

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

