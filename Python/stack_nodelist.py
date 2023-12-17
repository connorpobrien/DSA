from __future__ import annotations
from typing import Optional, List, Any

class Node:
    def __init__(self, value:Any, next:Optional[Node]):
        self.value = value
        self.next = next

    def __eq__(self, other:object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value and
                    self.next == other.next)
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.next))


class Stack:
    """Last-in first-out (LIFO) stack with a node list"""

    def __init__(self, top: Optional[Node] = None):
        self.top = top
        self.num_items = 0
        current = top
        while current is not None:
            self.num_items += 1
            current = current.next
    
    def __eq__(self, other:object) -> bool:
        if isinstance(other, Stack):
            return (self.top == other.top and
                    self.num_items == other.num_items)
        else:
            return False

    def __repr__(self) -> str:
        return ("Stack({!r})".format(self.top))

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item:Any) -> None:
        temp = self.top
        self.top = Node(item, Node)
        self.top.next = temp
        self.num_items += 1

    def pop(self) -> Any:
        if self.top is not None:
            temp = self.top 
            self.top = self.top.next
            self.num_items -= 1
            return temp.value
        else:
            raise IndexError("pop from empty stack")

    def peek(self) -> Any:
        if self.top is not None:
            return self.top.value
        else:
            raise IndexError("peek from empty stack")

    def size(self) -> int:
        return self.num_items
