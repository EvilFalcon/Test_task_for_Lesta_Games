#Циклический буфер FIFO
#Реализация 1: С использованием списка
from lib2to3.pytree import Node


class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if (self.tail + 1) % self.capacity == self.head:
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        if self.head == self.tail:
            raise IndexError("Buffer is empty")
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        return value

    def __len__(self):
        return (self.tail - self.head) % self.capacity

    # Реализация 2: С использованием двусвязного списка

    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    class CircularBufferLinkedList:
        def __init__(self, capacity):
            self.capacity = capacity
            self.head = None
            self.tail = None
            self.size = 0

        def enqueue(self, value):
            if self.size == self.capacity:
                raise OverflowError("Buffer is full")
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.size += 1

        def dequeue(self):
            if self.size == 0:
                raise IndexError("Buffer is empty")
            value = self.tail.value
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = self.head
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
            self.size -= 1
            return value

        def __len__(self):
            return self.size