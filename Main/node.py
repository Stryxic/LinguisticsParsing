from typing import Optional, List
import linknature, link

class Node:
    """Class representation of a generic node.
    """

    def __init__(self, id:int, name: str="", content: Optional[str] = None) -> None:
        """Initializes object. Only required variable is the ID, others can be set when required.
        
        """

        self.id = id
        self.name = name
        self.content = content
        self.links  = []

    def __repr__(self) -> str:
        return f"Node({self.id},{self.name})"

    def __str__(self) -> str:
        return f"{self.id}-{self.name}"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Node) and self.id == other.id and self.name == other.name and sorted(self.links,key=lambda x: x.id) == sorted(other.links,key=lambda x:x.id)
    
    def __hash__(self) -> int:
        return(hash(self.id))
    
    def set_contents(self, contents):
        self.contents = contents

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def add_link(self, link):
        self.links.append(link)

    def get_children(self):
        return [link.get_end() for link in self.links if link.nature == linknature.LinkNature.CHILD]
    
    def get_name(self):
        return self.name
    
    def get_contents(self):
        return self.content
    