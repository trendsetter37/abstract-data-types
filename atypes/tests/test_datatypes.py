# -*- coding: utf-8 -*-

import unittest

from atypes import Stack


class TestStackMethods(unittest.TestCase):

    def setUp(self):
        self.first_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        pass

    def test_clear(self):
        stack = Stack(self.first_list)
        print(stack)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
