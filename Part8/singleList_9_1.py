import unittest


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while self.head.next.next:
                self.head = self.head.next
            self.head.next = None
            self.tail = self.head
        self.length -= 1
        return node

    def merge(self, other):
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
            self.length = other.length
        else:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length

    def clear(self):
        self.length = 0
        self.head = None
        self.tail = None


class Test(unittest.TestCase):
    def setUp(self):
        self.alist = SingleList()
        self.alist.insert_head(Node(1))
        self.alist.insert_head(Node(2))

        self.blist = SingleList()
        self.blist.insert_head(Node(10))
        self.blist.insert_head(Node(20))

        self.clist = SingleList()

    def test_remove_tail(self):
        self.assertEqual(self.alist.remove_tail().data, 1)
        with self.assertRaises(ValueError):
            self.clist.remove_tail()

    def test_merge(self):
        self.alist.merge(self.blist)
        self.assertEqual(self.alist.length, 4)
        self.assertEqual(self.alist.head.data, 2)
        self.assertEqual(self.alist.tail.data, self.blist.tail.data)
        self.clist.merge(self.blist)
        self.assertEqual(self.clist.head.data, self.blist.head.data)

    def test_clear(self):
        self.alist.clear()
        self.assertIsNone(self.alist.head)
        self.assertIsNone(self.alist.tail)
        self.assertEqual(self.alist.length, 0)


if __name__ == '__main__':
    unittest.main()
