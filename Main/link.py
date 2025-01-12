import linknature

class Link:

    def __init__(self, start, id, nature=None, end=None) -> None:
        self.id = id
        self.nature = nature or linknature.LinkNature.OTHER
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"Link({self.id},{self.nature}, {self.start} -> {self.end})"
    
    def __str__(self) -> str:
        return f"{self.start}-[{self.nature}]->{self.end}"
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Link) and self.nature == other.nature and self.start == other.start and self.end == other.end
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def set_start(self, node):
        self.start = node
    
    def set_end(self, node):
        self.end = node

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
    
    def get_id(self):
        return self.id
    
    def get_terminals(self):
        if self.end:
            return [self.start, self.end]
        else:
            return [self.start]
        
    def set_nature(self, nature):
        if isinstance(nature, linknature.LinkNature):
            self.nature = nature
        else:
            raise ValueError("Invalid Nature.")
        
    

    
