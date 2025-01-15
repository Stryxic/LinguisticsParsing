from tree import Tree

class Document():
    

    def __init__(self) -> None:
        self.text = ""
        self.trees = []
        self.total_tree = None

    def set_trees(self, trees):
        self.trees = trees


    def trees_to_strings(self, transversal="dfs"):
        output_str = ""
        for tree in self.trees:
            tree_traversal = tree.traverse_tree(tranversal_type=transversal)[0]
            tree_contents = " ".join([x.contents for x in tree_traversal])
            output_str += tree_contents + "\n"
        return output_str        

    def trees_reordering(self):
        total_nouns = set()
        noun_node_dict = {}
        distinct_nouns = []
        result_tree_nodes = []
        result_tree_links = []
        for tree in self.trees:
            nodes = tree.traverse_tree(tranversal_type="dfs")[0]
            for node in nodes:
                contents = node.contents
                if contents not in total_nouns:
                    distinct_nouns.append(node)
                    noun_node_dict[contents] = node
                    total_nouns.add(contents)
                    links = node.get_links()
                    for link in links:
                        if link not in result_tree_links:
                            if len(link.get_terminals()) == 2:
                                result_tree_links.append(link)
                    result_tree_nodes.append(node)
                else:
                    links = node.get_links()
                    for link in links:
                        terminals = link.get_terminals()
                        if len(terminals) == 2:
                            # second_node = terminals[1]
                            first_occurance = noun_node_dict[contents]
                            link.set_start(first_occurance)
                            result_tree_links.append(link)
                        
        result_tree = Tree(result_tree_nodes[0], result_tree_nodes[1], result_tree_links[0], 1)
        remaining_nodes = result_tree_nodes[2:]
        remaining_links= result_tree_links[1:]
        added_ids = set()

        for node in remaining_nodes:
            result_tree.add_node(node)
            added_ids.add(node.id)

        for link in remaining_links:
            link_start = link.get_start()
            if link_start.id in added_ids:
                current_links = link_start.get_links()
                if link not in current_links:
                    result_tree.add_node_link(link_start.id, link)
            else:
                result_tree.add_link(link)
        

        tree_nodes = result_tree.get_nodes()
        visited_ids = set()
        total_ids = set()
        total_contents = set()
        visited_contents = set()
        node_chains = {}
        for node_id in tree_nodes:
            if node_id not in total_ids and contents not in visited_contents:
                output = self.recurse_node(tree_nodes[node_id], total_ids, visited_contents, 0)
                node_chains[tree_nodes[node_id].contents] = output

        return (node_chains, tree_nodes)
            



    def recurse_node(self, node, visited_ids, visited_contents, depth):
        total_dicts = []
        if node:
            if node.id not in visited_ids and node.contents not in visited_contents:
                node_links = node.get_links()
                visited_ids.add(node.id)
                visited_contents.add(node.contents)   
                for link in node_links:
                    end = link.get_end()
                    if end:
                        if end.contents:
                            depth += 1
                            total_dicts.append(self.recurse_node(end, visited_ids, visited_contents, depth))
                if node.contents:
                    total_dicts.append({node.id:node.contents})
                    return total_dicts
            else:
                total_dicts.append({node.id:node.contents})
                return total_dicts
        else:
            return total_dicts
        