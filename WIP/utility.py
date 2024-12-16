#This will hold the most used functions across all of the documents, the core functionality.


#Node - The basic unit of anything in the system. Very generic, abstract.

class Node():

    #Each node has an identity (an ID number), a name, zero to many links, and whatever it contains. The contents are generic, links are a specific type, id is an int, and name is a string.
    id = 0
    name = ""
    links = []
    content = None


    def __init__(self) -> None:
        return True
    
    def __init_subclass__(cls) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def set_contents(self, contents):
        self.content = contents


    #A link is a different object. It contains a start point, an end point, and a type. The link can either be from or to the node. 
    def add_link(self, link):
        self.links.append(link)

    def get_children(self) -> object:
        children = []
        for link in self.links:
            if link == "child":
                children.append(link)
        return children



#Link - Any connection between one Node and another Node
    
class Link():
    id = 0
    nature = None
    start = None
    end = None

    #all links must at the least have a starting node. A link with no terminal is a possible, but not actualised, connection.
    def __init__(self, node) -> None:
        self.start = node

    #terminal of the link. Each link can only have one starting node, and one ending node. These nodes can also act as greater subgroup of several nodes.
    def set_end(self, node) -> None:
        self.end = node


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
    def __init__(self, node_1:Node, node_2:Node, link:Link) -> bool:
        self.nodes.append(node_1)
        self.nodes.append(node_2)
        self.links.append(link)
        if link.start == node_1 and link.end == node_2:
            return True
        else:
            return False
        
    