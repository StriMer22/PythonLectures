"""
Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. Poprawić metodę put() 
w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek. 
Napisać kod testujący kolejkę.
"""


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # current size of the array
        self.items = self.n * [None]
        self.head = 0           # first to take
        self.tail = 0           # first free

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        data = self.items[self.head]
        self.items[self.head] = None      # removing the reference
        self.head = (self.head + 1) % self.n
        return data
