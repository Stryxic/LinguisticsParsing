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
    
    #Takes all nodes and links, and outputs an array of various node selections.
    def tree_to_string(self):
        output_string = ""
        output_array = []
        #First, get the tree traversal
        traversal_output = self.traverse_tree()
        #We return the tree itself
        traversal_tree = traversal_output[0]
        #From here we want the Depth map
        depth_map = traversal_output[1]
        #Converts an ID to its depth in the depth map
        ids_to_depths = {x[1][0].id:x[0] for x in depth_map.items()}
        #Finds all terminals from all the links in the tree
        link_terminals=[(x.get_start().id,x.get_end().id) for x in self.links]

        #Iterating through links,
        for terminals in link_terminals:
            #Get the ID of the first node for looking up
            start_node_id = terminals[0]
            #Get the ID of the second node for look up
            end_node_id = terminals[1]
            #If it exists in the dictionary retrieve it, else if its end is there use that node. If none are found, none are added.
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

            #If the difference between the depths of the nodes is greater than 1, rearrange them

            if abs(end_node_depth-start_node_depth)>1:
                if start_node_depth < end_node_depth:
                    ids_to_depths[end_node_id] = start_node_depth+1
                else:
                    ids_to_depths[start_node_id] = end_node_depth-1

        #Array representation of the tree
        array_tree_repr = []

        max_depth = -1
        #Iterating through each ID through each depth
        for id in ids_to_depths:
            #Finds the current depth for this ID
            current_depth = ids_to_depths[id]
            #If it is larger than the max depth, add this ID to the array, and change the max depth. Otherwise add it to the array at its index.
            if current_depth > max_depth:
                array_tree_repr.append([id])
                max_depth = current_depth
            else:
                if current_depth < len(array_tree_repr):
                    array_tree_repr[current_depth].append(id)

        all_nodes = []
        final_nodes = []
        #For each node that can be represented as 1 depth between each other at one point in the text,
        for element in array_tree_repr:
            #If the node exists and has content, it is usable
            current_nodes = [self.nodes[x] for x in element if x in self.nodes and self.nodes[x].content]
            node_to_children = {x.content:x.get_children() for x in current_nodes}
            #Retrieve the contents of all current nodes
            contents = [x.content for x in current_nodes]
            #Checking to ensure we can iterate through the array
            if contents and contents != [None]:
                #Separate arrays at the current depth, and in total
                all_nodes += contents
                final_nodes.append(current_nodes)
        #Finding the links between allowed nodes
        spanning_links = []
        #For all the links in the tree,
        for link in self.links:
            #If the link starts or ends with an allowed node, add it to a spanning tree
            if link.get_start().content in all_nodes or link.get_end().content in all_nodes:
                spanning_links.append(link)

        #Return the spanning tree, the array of nodes at each level, and all nodes in total.
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

