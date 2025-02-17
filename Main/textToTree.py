from node import Node
from link import Link
from linknature import LinkNature
from tree import Tree

class TreeConverter():

    def __init__(self) -> None:
        #Initializing the total nouns the overall tree will consist of. All the nodes will be part of this tree, although some may reoccur multiple times.
        self.nouns = {}
        self.total_nodes = {}
        self.total_links = {}
        self.total_trees = {}
        self.node_count = 0
        self.link_count = 0
        self.tree_count = 0
    
    def set_nouns(self, noun_list):
        self.nouns = noun_list

    def reset_contents(self):
        self.nouns = {}
        self.total_nodes = {}
        self.total_links = {}
        self.total_trees = {}
        self.node_count = 0
        self.link_count = 0
        self.tree_count = 0

    def convert_sentence(self, nouns):
        #Each list of nouns (i.e. sentence) is turned into its own tree. This is a preprocessing step, to convert it from text into the first form of our overall document.
        current_node = None
        current_link = None
        sentence_nodes = []
        sentence_links = []        

        #Once it has an array of nouns, 
        node_index = 0
        for noun in nouns:
            self.node_count += 1
            new_node = Node(self.node_count)
            new_node.set_contents(noun)
            new_node.set_name("Noun")
            current_node = new_node
            current_node.content = noun
            self.total_nodes[current_node.id] = current_node
            sentence_nodes.append(current_node)
            if current_link:
                current_link.set_end(current_node)
            self.link_count += 1
            current_link = Link(current_node, self.link_count, LinkNature.CHILD)
            self.total_links[current_link.id] = current_link
            sentence_links.append(current_link)
            current_node.add_link(current_link)
            node_index += 1
        self.tree_count += 1
        current_tree = Tree(sentence_nodes[0], sentence_nodes[1], sentence_links[0], self.tree_count)
        remaining_nodes = sentence_nodes[2:]
        remaining_links = sentence_links[1:]
        if remaining_nodes:
            for node in remaining_nodes:
                current_tree.add_node(node)
        if remaining_links:
            for link in remaining_links:
                current_tree.add_link(link)
        return current_tree
    



