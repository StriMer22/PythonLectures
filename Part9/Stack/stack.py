"""
Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu.
Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku 
przepełnienia stosu. Napisać kod testujący stos.
"""


class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False  # It's never full

    def push(self, item):
        if self.is_full():
            raise ValueError("stack is full")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")
        return self.items.pop()
