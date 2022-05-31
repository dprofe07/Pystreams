import sys
from .special import returner
from .flags import Flag


class stringstreamFlags:
    def __init__(self, tip=None, buff=None, flag=None):
        self.type = tip if callable(tip) else (lambda x: x)
        self._buffer = buff or []
        self.flag = flag or Flag()

    def __lshift__(self, other):
        if hasattr(other, '__iter__'):
            self._buffer.extend(other)
        else:
            self._buffer.append(other)
        return self
    def __rshift__(self, other):
        if callable(other):
            return self.__class__(other, self._buffer, self.flag)
        elif isinstance(other, Flag):
            return self.__class__(self.type, self._buffer, other | self.flag)
        elif other == returner:
            return self._call_self_type(other, 'BUFFER_POP', 'RETURNED')
        else:
            if not self._buffer:
                raise ValueError('Buffer is empty')
            self._call_self_type(other, 'BUFFER_POP', 'TO_MAIN')
            return self

    def __rlshift__(self, other):
        while self._buffer:
            other << self._buffer.pop()
    def __rrshift__(self, other):
        while other._buffer:
            self << other._buffer.pop()
    def __repr__(self):
        return '<stringstream = {' + ', '.join(map(lambda x: '"' + x + '"' if type(x) == str else x, self._buffer)) + '}>'
    def flush(self):
        self._buffer.clear()
    def getBuffer(self):
        return self._buffer.copy()
