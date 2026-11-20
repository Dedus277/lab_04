import unittest

from algolab4 import Stack


class StackTests(unittest.TestCase):
    def test_lifo(self):
        stack = Stack()
        stack.push("first")
        stack.push("second")
        self.assertEqual(stack.pop(), "second")
        self.assertEqual(stack.pop(), "first")

    def test_peek_preserves_top_and_size(self):
        stack = Stack()
        stack.push("bottom")
        marker = object()
        stack.push(marker)
        self.assertEqual(len(stack), 2)
        self.assertTrue(stack)
        self.assertIs(stack.peek(), marker)
        self.assertIs(stack.peek(), marker)
        self.assertEqual(len(stack), 2)
        self.assertIs(stack.pop(), marker)
        self.assertEqual(stack.peek(), "bottom")
        self.assertEqual(len(stack), 1)

    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        self.assertFalse(stack)
        stack.push(None)
        self.assertTrue(stack)
        self.assertIsNone(stack.pop())
        self.assertFalse(stack)
        self.assertEqual(len(stack), 0)
        for operation in (stack.peek, stack.pop):
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(IndexError):
                    operation()
