# -*- coding: utf-8 -*-


class StackEmptyError(TypeError):
    def __init__(self, *args, **kwargs):
        if errmsg is not None:
            super(TypeError, self).__init__(*args, **kwargs)

            
