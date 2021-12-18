import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

        self.stack1.push(10)
        self.stack1.push(20)
        self.stack1.push(30)

        self.stack2.push(1)
        self.stack2.push(2)
        self.stack2.push(3)

        self.stack_empty = Stack()

    def test__str__(self):
        self.assertEqual('[10, 20, 30]', str(self.stack1))
        self.assertEqual('[1, 2, 3]', str(self.stack2))
        self.assertEqual('[]', str(self.stack_empty))

    def test_is_empty(self):
        self.assertTrue(self.stack_empty.is_empty())
        self.assertFalse(self.stack1.is_empty())
        self.assertFalse(self.stack2.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack1.is_full())
        self.assertFalse(self.stack2.is_full())
        self.assertFalse(self.stack_empty.is_full())

    def test_push(self):
        self.stack2.push(1)
        self.stack_empty.push(1)
        self.assertEqual('[1, 2, 3, 1]', str(self.stack2))
        self.assertEqual('[1]', str(self.stack_empty))

    def test_pop(self):
        self.stack2.push(1)
        self.stack_empty.push(1)
        self.stack2.pop()
        self.stack_empty.pop()
        self.test__str__()


if __name__ == '__main__':
    unittest.main()
