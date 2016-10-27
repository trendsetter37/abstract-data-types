# -*- coding: utf-8 -*-

from exceptions import StackEmptyError


class Stack(object):
    
    _accepted_seqs = (list, tuple, set)
    _stack = list()

    def __init__(self, *args):
       
        if len(args) == 0:
            self._stack = list()
        else:
            self._stack.extend(args)
    
    def clear(self):
        try:
            assert self.length != 0
        except AssertionError:
            raise StackEmptyError
        self._stack = list()

    def pull(self):
        ''' pull value from top of stack
        '''
        if self.length > 0:
            return self._stack.pop()
        else:
            raise StackEmptyError('Stack is empty')

    def push(self, *args):
        ''' push new value or sequence of values onto the stack
        '''
        self._stack.extend(args)

    def __iter__(self):
        for thing in self._stack:
            yield thing

    def __repr__(self):
        return "Stack({})".format(self._stack)

    def __str__(self):
        return "{}".format(self._stack)

    @property
    def length(self):
        return len(self._stack)
