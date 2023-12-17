from __future__ import annotations
from typing import Optional, List, Any

class Node:
    def __init__(self, value:Any, next:Optional[Node]=None) -> None:
        self.value = value
        self.next = next

    def __eq__(self, other:object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value and
                    self.next == other.next)
        else:
            return False

    def __repr__(self) -> str:
        return "Node({!r}, {!r})".format(self.value, self.next)
    

class Queue:
    def __init__(self, rear:Optional[Node]=None, front:Optional[Node]=None, num_items:int=0) -> None:
        self.rear = rear
        self.front = front
        self.num_items = num_items

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return (self.rear == other.rear and
                    self.front == other.front and
                    self.num_items == other.num_items)
        else:
            return False
        
    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.rear, self.front))
    
    def get_items(self) -> List[Any]:
        items = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.next
        if self.rear is not None:
            rear_items = []
            rear = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.next
            items.extend(rear_items[::-1])
        return items
    
    def is_empty(self) -> bool:
        return self.num_items == 0
    
    def enqueue(self, item:Any) -> None:
        if self.rear is None:
            self.rear = Node(item, None)
            self.num_items += 1
        else:
            self.rear = Node(item, self.rear)
            self.num_items += 1

    def size(self) -> int:
        return self.num_items
    
    def dequeue(self) -> Any:
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        (This will still satisfy O(1) requirement for the operation,
        as the transfer is amortized across all dequeues)
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""
        # normal case
        if self.front:
            temp = self.front 
            self.front = self.front.next
            self.num_items -= 1
            return temp.value

        # self.front is empty but self.rear is not
        elif self.rear:
            self.front = Node(self.rear.value, None)
            self.rear = self.rear.next 

            while self.rear:
                temp = self.front
                self.front = Node(self.rear.value, temp)
                self.rear = self.rear.next
            
            temp = self.front
            self.front = self.front.next
            self.num_items -= 1
            return temp.value
    
        else:
            raise IndexError("dequeue from empty queue")
    