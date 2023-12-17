from typing import Optional, List, Any

class Queue:
    def __init__(self, capacity:int, init_items:Optional[List[Any]]=None) -> None:
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.rear = 0
        if init_items:
            for item in init_items:
                self.enqueue(item)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Queue):
            return (self.capacity == other.capacity and
                    self.items == other.items and
                    self.num_items == other.num_items and
                    self.front == other.front and
                    self.rear == other.rear)
        else:
            return False
        
    def __repr__(self) -> str:
        return ("Queue({!r}, {!r})".format(self.capacity, self.get_items()))
    
    def get_items(self) -> List[Any]:
        if self.num_items == 0:
            return []
        elif self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]
        
    def is_empty(self) -> bool:
        return self.num_items == 0
    
    def is_full(self) -> bool:
        return self.num_items >= self.capacity
    
    def enqueue(self, item:Any) -> None:
        if self.is_full():
            self.capacity *= 2
            new_items = [None] * self.capacity
            for i in range(self.num_items):
                new_items[i] = self.items[(self.front + i) % self.num_items]
            self.items = new_items
            self.front = 0
            self.rear = self.num_items
        self.items[self.rear] = item
        self.rear += 1
        self.num_items += 1

    def dequeue(self) -> Any:
        if self.num_items > 0:
            temp = self.items[self.front]
            self.front += 1
            self.num_items -= 1
            return temp
        else:
            raise IndexError("dequeue from empty queue")
        
    def size(self) -> int:
        return self.num_items
    
    def peek(self) -> Any:
        if self.num_items > 0:
            return self.items[self.front]
        else:
            raise IndexError("peek from empty queue")
