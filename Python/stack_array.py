from typing import Optional, List, Any

class Stack:
    """Last-in first-out (LIFO) stack with a Python list"""

    def __init__(self, capacity:Optional[int], init_items:Optional[List[Any]]=None) -> None:
        """Create a new stack with optional initial capacity"""
        self._capacity = capacity if capacity else 1
        self.items = [None] * capacity
        self.num_items = 0
        if init_items:
            for item in init_items:
                self.push(item)

    def __eq__(self, other:object) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def is_empty(self) -> bool:
        pass

    def is_full(self) -> bool:
        pass    

    def push(self, item:Any) -> None:
        pass    

    def pop(self) -> Any:
        pass    

    def peek(self) -> Any:
        pass

    def size(self) -> int:
        pass

    def get_capacity(self) -> int:
        pass
