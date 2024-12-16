#This will hold the most used functions across all of the documents, the core functionality.


#Node - The basic unit of anything in the system. Very generic, abstract.

class Node():

    id = 0
    name = ""
    links = []


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


    def get_children(self) -> object:
        children = []
        for link in self.links:
            if link == "child":
                children.append(link)
        return children




#Link - Any connection between one Node and another Node

#Tree - The collection of Links and Nodes