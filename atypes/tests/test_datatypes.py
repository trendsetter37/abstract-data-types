# -*- coding: utf-8 -*-

import unittest

from atypes import Stack
from atypes.exceptions import StackEmptyError


class TestStackMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clear(self):
        stack = Stack(*[x for x in range(1, 6)])
        self.assertEqual(stack.length, 5)
        stack.clear()
        self.assertEqual(stack.length, 0)

    def test_peek(self):
        stack = Stack()
        stack.push(35)
        self.assertEqual(stack.peek(), 35)

    def test_pull(self):
        stack = Stack(*[x for x in range(1, 6)])
        old_length = stack.length
        self.assertEqual(stack.pull(), 5)
        self.assertLess(stack.length, old_length)

    def test_push(self):
        stack = Stack()
        stack.push(77)
        self.assertEqual(stack.peek(), 77)

    def test_stack_length(self):
        stack = Stack()
        stack.push(6)
        self.assertEqual(stack.length, 1)

    def test_stack_loading(self):
        stack = Stack()
        stack.push(*[x for x in range(1, 101)])
        self.assertEqual(stack.length, 100)
        self.assertEqual(stack.pull(), 100)

    def test_empty_stack_error(self):
        stack = Stack()
        with self.assertRaises(StackEmptyError):
            stack.pull()


if __name__ == '__main__':
    unittest.main()
