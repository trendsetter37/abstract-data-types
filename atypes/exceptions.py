# -*- coding: utf-8 -*-


class StackEmptyError(Exception):
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)

__all__ = [
    "StackEmptyError"
]
