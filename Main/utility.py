#This will hold the most used functions across all of the documents, the core functionality.


#Node - The basic unit of anything in the system. Very generic, abstract.

class Node():

    #Each node has an identity (an ID number), a name, zero to many links, and whatever it contains. The contents are generic, links are a specific type, id is an int, and name is a string.
    id = 0
    name = ""
    links = []
    content = None


    def __init__(self, id) -> None:
        self.id = id
        self.links = []
        self.content = None
        self.name = ""
    
    def __init_subclass__(cls) -> None:
        pass


    def __repr__(self) -> str:
        return str(self.id)

    def __str__(self) -> str:
        return str(f"{self.id}-{self.name}")

    def __eq__(self, __value: object) -> bool:
        if self.name == __value.name and self.content == __value.content and self.links == __value.links:
            return True
        else:
            return False

    def set_contents(self, contents):
        self.content = contents

    def set_name(self, name):
        self.name = name


    #A link is a different object. It contains a start point, an end point, and a type. The link can either be from or to the node. 
    def add_link(self, link):
        self.links.append(link)

    def get_children(self) -> object:
        children = []
        for link in self.links:
            if link == "child":
                children.append(link)
        return children

    def get_name(self):
        return self.name
    
    def get_contents(self):
        return self.content


#Link - Any connection between one Node and another Node
    
class Link():
    id = 0
    nature = None
    start = None
    end = None

    #all links must at the least have a starting node. A link with no terminal is a possible, but not actualised, connection.
    def __init__(self, node, id) -> None:
        self.start = node
        self.id = id
        self.nature = None
        self.end = None

    def __repr__(self) -> str:
        return f"{self.id}:{self.nature}"

    def __str__(self) -> str:
        return f"{self.start}-[{self.nature}]->{self.end}"
    
    

    #terminal of the link. Each link can only have one starting node, and one ending node. These nodes can also act as greater subgroup of several nodes.
    def set_end(self, node) -> None:
        self.end = node

    def get_end(self) -> Node:
        return self.end
    
    def get_start(self) -> Node:
        return self.start
    
    def get_id(self) -> int:
        return self.id

    def get_terminals(self):
        if self.end:
            return [self.start.get_contents(), self.end.get_contents()]
        else:
            return [self.start.get_contents()]

    #A nature is a type of fixed, limited domain of features. It would be best represented as some type of enum.
    def set_nature(self, nature) -> None:
        self.nature = nature

    #A link is equal to another link if its start, end, and nature are equivalent. 
    def __eq__(self, __value: object) -> bool:
        if __value.start:
            if self.nature == __value.nature and self.start == __value.start and self.end == __value.end:
                return True
            else:
                return False
        else:
            return False



#Tree - The collection of Links and Nodes
        

class Tree():
    id = 0
    nodes = []
    links = []


    #The minimal tree is a Node -> Node
    def __init__(self, node_1:Node, node_2:Node, link:Link, id) -> None:
        self.nodes = []
        self.links = []
        self.nodes.append(node_1)
        self.nodes.append(node_2)
        self.links.append(link)
        self.id = id
        
    def get_nodes(self) -> Node:
        return self.nodes
        
    def get_links(self) -> Link:
        return self.links
    
    def add_node(self, node:Node):
        self.nodes.append(node)
    
    def remove_node(self, id):
        removal = None
        for node in self.nodes:
            if node.id == id:
                removal = node
                break
        if removal:
            self.nodes.remove(removal)

    def add_link(self, link:Link):
        if link.end:
            if link.get_end() not in self.nodes:
                self.add_node(link.get_end())
        self.links.append(link)
    
    def remove_link(self, id):
        pos = 0
        for i in range (0, len(self.links)):
            link = self.links[i]
            if link.get_id() == id:
                pos = i
        if pos:
            self.links.pop(pos)


    def __str__(self) -> str:
        tree_str = ""
        for link in self.links:
            tree_str += str(link) + "\n"

        tree_str = tree_str.strip()
        return tree_str
    
    #Gives a better representation for the whole tree, without overriding _repr_ if I need it later.
    def traverse_tree(self) -> str:
        output_str = ""
        for link in self.links:
            terminals = link.get_terminals()
            if len(terminals) == 2:
                if output_str:
                    output_str += f"{terminals[1]}#{link.get_end().get_name()}->"
                else:
                    output_str += f"{terminals[0]}#{link.get_start().get_name()}->{terminals[1]}#{link.get_end().get_name()}->"
        return output_str


#Parsing the tree we just made.
class TreeParser():
    tree = None
    noun_list = []
    noun_dict = {}
    #Storing a list of all nouns, and the count.
    def __init__(self, tree):
        self.tree = tree
        self.noun_list = []
        self.noun_dict = {}

    #Check what kind of node it is, and parse it.
    def parse_tree(self):
        links = self.tree.get_links()
        for link in links:
            start_node = link.get_start()
            end_node = link.get_end()
            self.parse_node(start_node, 1)
            if end_node:
                self.parse_node(end_node, 2)
        self.count_nouns()

    #Trees have nodes to be parsed, so recusrively call the parse node function
    def parse_tree_node(self, node):
        tree = node.get_contents()
        node_links = tree.get_links()
        if node_links: 
            for link in node_links:
                first_node = link.get_start()
                second_node = link.get_end()
                self.parse_node(first_node, 1)
                if second_node:
                    self.parse_node(second_node, 2)

    #Text contains a noun, and a noun type
    def parse_text_node(self, node):
        noun_type = node.get_name()
        noun = node.get_contents()
        self.noun_list.append([noun,noun_type])

    #A node can either be a tree, or text.
    def parse_node(self, node, pos):
        node_name = node.get_name()
        if pos == 1:
            if node_name == "Tree":
                self.parse_tree_node(node)
            else:
                self.parse_text_node(node)

    def get_nouns(self):
        return self.noun_list
    
    #Simple pythonic invocation to convert a list into a count
    def count_nouns(self):
        for noun in self.noun_list:
            noun = noun[0].lower()
            if noun in self.noun_dict.keys():
                self.noun_dict[noun] += 1
            else:
                self.noun_dict[noun] = 1
                
    def get_counts(self):
        return self.noun_dict
