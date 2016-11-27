# -*- coding: utf-8 -*-


class Leaf(object):
    def __init__(self, left=None, right=None):
        self.left, self.right = left, right


class Node(object):
    def __init__(self, child=None):
        self.child = child
