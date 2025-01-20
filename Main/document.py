from tree import Tree
from node import Node
from link import Link
from linknature import LinkNature

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

#Iterates through the array of trees, performing depth first search on the first node of each tree to get every element, then operating from there.
    def trees_reordering(self):
        #After parsing through the list, we store a set of all nouns (the contents of nodes), nodes for the tree, and links for the tree.
        total_nouns = set()
        noun_node_dict = {}
        distinct_nouns = []
        result_tree_nodes = []
        result_tree_links = []
        id_to_node = {}
        sentence_nodes = {}
        sentence_node_id = 1
        intra_sentence_link = None
        sentence_links = {}

        

        #Iterating through each tree in the list
        for tree in self.trees:
            #Creating each sentence as a node to manage successive sentences. This allows for the each sentence tree to terminate with a None contents, to indicate the end of
            #the sentence. Then, the sentence itself (the contents of all nouns) is implicitly that tree, wrapped into an object and given an ID.
            #This allows it to be placed as the start and end point of a link, which can join multiple sentences together. This can allow for
            #a None terminator to indicate the end of a paragraph, which in turn could be contained within a paragraph node, and so on. This can
            #construct an entire document, where the final None content is the end of that particular document. The depth of each sentence can be
            #the minimum depth of all nodes within the sentence.
            sentence_node = Node(sentence_node_id, "Sentence", tree)
            sentence_nodes[sentence_node_id] = sentence_node

            if intra_sentence_link:
                intra_sentence_link.set_end(sentence_node)
                   
            #Using a different type of nature to separate the sentences as a new class of link, to allow for easier searching later on
            intra_sentence_link = Link(sentence_node, sentence_node_id, LinkNature.PARENT)
            sentence_links[sentence_node_id] = intra_sentence_link
            sentence_node_id += 1
            #Collecting all linked nodes in the tree
            nodes = tree.traverse_tree(tranversal_type="dfs")[0]
            # print(nodes)
            #Iterating through each node in the tree, first to last.
            for node in nodes:
                #Contents = The noun
                contents = node.content
                id = node.id
                id_to_node[id] = node
                # print(node.content)
                #If it has not been added to the set of visited nouns, create it.
                if contents not in total_nouns:
                    #Adding it to distinct nodes
                    distinct_nouns.append(node)
                    #Setting the element of the node dictionary at the noun string, to the node containing it.
                    noun_node_dict[contents] = node
                    #set of total nouns now includes visited noun
                    total_nouns.add(contents)
                    #Getting all links from the node
                    links = node.get_links()
                    #Iterate through each link
                    for link in links:
                        #If that link has not already been added to result tree links
                        if link not in result_tree_links:
                            #If the link has both a start and an end, add it to result_tree_links
                            if len(link.get_terminals()) == 2:
                                link_node_1 = link.get_start()
                                link_node_2 = link.get_end()
                                if link_node_1.content:
                                    if link_node_1 not in result_tree_nodes:
                                        result_tree_nodes.append(link_node_1)
                                if link_node_2.content:
                                    if link_node_2 not in result_tree_nodes:
                                        result_tree_nodes.append(link_node_2)

                                result_tree_links.append(link)
                    #Add that node to the total array of all nodes
                    result_tree_nodes.append(node)
                    #If contents is already in total_nouns
                else:
                    #total_nouns.add(contents)
                    #Get that node's links
                    links = node.get_links()
                    result_tree_nodes.append(node)
                    existing_node = noun_node_dict[contents]
                    #Iterating through each link
                    for link in links:
                        #Getting the terminals (start and end of the link)
                        terminals = link.get_terminals()
                        #If there is a start and an end
                        # if len(terminals) == 2:
                        # print(f"{second_node.id}:{second_node.content}")
                            #Takes the first node, and creates a link using it. !!!Should add this link to the node as well.
                        link.set_start(existing_node)
                        if len(terminals) == 2:
                            second_node = terminals[1]
                            if second_node:
                                if second_node.content:  
                                    existing_node.add_link(link)                      
                        # if second_node:
                        #     link.set_end(second_node)
                            #Adds the link to the total links
                        result_tree_links.append(link)
                        
        #print(result_tree_nodes)
        # if len(result_tree_nodes) == 1:
        #     return None
        print(sentence_nodes)                
        
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
        print(tree_nodes)
        for node_id in tree_nodes:
            if node_id not in total_ids and contents not in visited_contents:
                output = self.recurse_node(tree_nodes[node_id], total_ids, visited_contents, 0)
                node_chains[tree_nodes[node_id].content] = output

        print("|||||||||||||||################|||||||||||||||||")
        print(node_chains)
        print(tree_nodes)
        return (node_chains, tree_nodes)
            



    def recurse_node(self, node, visited_ids, visited_contents, depth):
        total_dicts = []
        print(node)
        if node:
            print(node.id, node.content)
            if node.id not in visited_ids and node.content not in visited_contents:
                print("Visiting links")
                node_links = node.get_links()
                visited_ids.add(node.id)
                visited_contents.add(node.content)   
                for link in node_links:
                    end = link.get_end()
                    if end:
                        total_dicts.append(self.recurse_node(end, visited_ids, visited_contents, depth+1))
                if node.content:
                    total_dicts.append({node.id:node.content})
                    return total_dicts
            else:
                total_dicts.append({node.id:node.content})
                return total_dicts
        else:
            return total_dicts
        