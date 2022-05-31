import sys
from .special import returner
from .stringstreamFlags import stringstreamFlags
from .flags import Flag

class stringstream(stringstreamFlags):
    def __init__(self, tip=None, buff=None, flags=None):
        super().__init__(tip, buff)
    def __rshift__(self, other):
        if isinstance(other, Flag):
            return self.__class__(other, self._buffer)
        else:
            return super().__rshift__(other)
