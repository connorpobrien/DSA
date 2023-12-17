from typing import Optional, List, Any

class Stack:
    """Last-in first-out (LIFO) stack with a Python list"""

    def __init__(self, capacity:Optional[int], init_items:Optional[List[Any]]=None) -> None:
        """Create a new stack with optional initial capacity"""
        self.capacity = capacity if capacity else 1
        self.items = [None] * capacity
        self.num_items = 0
        if init_items:
            for item in init_items:
                self.push(item)

    def __eq__(self, other:object) -> bool:
        if isinstance(other, Stack):
            return (self.capacity == other.capacity and
                    self.items == other.items and
                    self.num_items == other.num_items)
        else:
            return False

    def __repr__(self) -> str:
        return ("Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items]))

    def is_empty(self) -> bool:
        return self.num_items == 0

    def is_full(self) -> bool:
        return self.num_items == self.capacity

    def push(self, item:Any) -> None:
        if self.is_full():
            self.capacity *= 2
            new_items = [None] * self.capacity
            for i in range(self.num_items):
                new_items[i] = self.items[i]
            self.items = new_items
        self.items[self.num_items] = item
        self.num_items += 1
        
    def pop(self) -> Any:
        if not self.is_empty():
            temp = self.items[self.num_items - 1]
            self.items[self.num_items - 1] = None
            self.num_items -= 1
            return temp
        else:
            raise IndexError("pop from empty stack")

    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[self.num_items - 1]
        else:
            raise IndexError("peek from empty stack")

    def size(self) -> int:
        return self.num_items

    def get_capacity(self) -> int:
        return self.capacity
