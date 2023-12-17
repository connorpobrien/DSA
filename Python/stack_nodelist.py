from __future__ import annotations
from typing import Optional, List, Any

class Node:
    def __init__(self, value:Any, rest:Optional[Node]):
        self.value = value
        self.next = next

    def __eq__(self, other:object) -> bool:
        pass

    def __repr__(self) -> str:  
        pass


class Stack:
    """Last-in first-out (LIFO) stack with a node list"""

    def __init__(self, top: Optional[Node] = None):
        self.top = top
        self.num_items = 0
        while top is not None:
            self.num_items += 1
            top = top.next
    
    def __eq__(self, other:object) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def is_empty(self) -> bool:
        pass

    def push(self, item:Any) -> None:
        pass

    def pop(self) -> Any:
        pass

    def peek(self) -> Any:
        pass

    def size(self) -> int:
        pass

    