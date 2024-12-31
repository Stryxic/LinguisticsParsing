from enum import Enum

class LinkNature(Enum):
    CHILD = "child"
    PARENT = "parent"
    SIBLING = "sibling"
    OTHER = "other"