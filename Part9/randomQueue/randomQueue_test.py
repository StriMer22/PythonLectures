import unittest
from randomQueue import RandomQueue


class TestRandomQueue(unittest.TestCase):

    def test_insert(self):
        q = RandomQueue(3)
        q.insert(10)
        q.insert(20)
        q.insert(30)
        self.assertTrue(q.is_full())
        with self.assertRaises(ValueError):
            q.insert(40)

    def test_remove(self):
        q = RandomQueue(1)
        q.insert(1)
        self.assertEqual(q.remove(), 1)
        self.assertTrue(q.is_empty())
        with self.assertRaises(ValueError):
            q.remove()

    def test_is_full(self):
        q = RandomQueue(3)
        q.insert(1)
        q.insert(2)
        self.assertFalse(q.is_full())
        q.insert(3)
        self.assertTrue(q.is_full())
        q.remove()
        self.assertFalse(q.is_full())

    def test_is_empty(self):
        q = RandomQueue(3)
        self.assertTrue(q.is_empty())
        q.insert(1)
        self.assertFalse(q.is_empty())

    if __name__ == '__main__':
        unittest.main()  # uruchamia wszystkie testy
