"""
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.
"""
import random


class RandomQueue:
    def __init__(self, size=5):
        self.n = size + 1         # current size of the array
        self.items = self.n * [None]
        self.head = 0           # first to take
        self.tail = 0           # first free

    def insert(self, item):
        if self.is_full():
            raise IndexError("random queue is full")
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise IndexError("random queue is empty")
        else:
            positionElement = random.randint(0, self.tail-1)
            data = self.items[positionElement]
            self.items[positionElement] = self.items[self.tail-1]
            self.tail = self.tail-1
            return data

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail
