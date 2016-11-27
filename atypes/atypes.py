# -*- coding: utf-8 -*-
''' The dtypes module contains all of the abstract data type
    classes.
'''

from .exceptions import StackEmptyError


class Stack(object):

    accepted_seqs = (list, tuple, set)
    _stack = list()

    def __init__(self, *args):

        if len(args) == 0:
            self._stack = list()
        else:
            self._stack.extend(args)

    def clear(self):
        self._check_stack_vacancy()
        self._stack = list()

    def peek(self):
        self._check_stack_vacancy()
        return self._stack[-1]

    def pull(self):
        '''Pull a value from the top of the stack.
        '''
        self._check_stack_vacancy()
        return self._stack.pop()

    def push(self, *args):
        '''Push new value or sequence of values onto stack.
        '''
        self._stack.extend(args)

    def _check_stack_vacancy(self):
        if len(self._stack) < 1:
            raise StackEmptyError('Stack is empty.')

    def __iter__(self):
        for thing in self._stack:
            yield thing

    def __repr__(self):
        stack_items = ""
        for idx, item in enumerate(self._stack):
            if idx != self.length - 1:
                stack_items += str(item) + ', '
            else:
                stack_items += str(item)
        return 'Stack({})'.format(stack_items)

    def __str__(self):
        return "{}".format(self._stack)

    @property
    def length(self):
        '''Return length of stack.
        '''
        return len(self._stack)


__all__ = [
    "Stack"
]
