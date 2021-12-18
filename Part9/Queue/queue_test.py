import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_is_empty(self):
        q = Queue(1)
        self.assertTrue(q.is_empty())
        q.put(1)
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        q = Queue(3)
        self.assertFalse(q.is_full())
        q.put(1)
        q.put(2)
        q.put(3)
        self.assertTrue(q.is_full())

    def test_put(self):
        q = Queue(3)
        q.put(1)
        q.put(2)
        q.put(3)
        with self.assertRaises(ValueError):
            q.put(4)

    def test_get(self):
        q = Queue(3)
        q.put(1)
        q.put(2)
        q.put(3)
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        self.assertEqual(q.get(), 3)
        with self.assertRaises(ValueError):
            q.get()


if __name__ == '__main__':
    unittest.main()
