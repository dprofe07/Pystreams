from .istreamFlags import istreamFlags, sys
from .flags import Flag

class istream(istreamFlags):
    def __init__(self, stream = sys.stdin, type_=None, flags=None):
        super().__init__(stream, type_)
    def __rshift__(self, other):
        if isinstance(other, Flag):
            return self.__class__(self.stream, other)
        else:
            return super().__rshift__(other)


pin = cin = istream(sys.stdin)