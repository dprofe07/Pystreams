import sys

from .flags import Flag
from .stringstream import stringstream
class ostreamFlags:
    def __init__(self, stream=sys.stdout, flag=None):
        self.stream = stream
        self.flag = flag or Flag()
    def __lshift__(self, other):
        if isinstance(other, Flag):
            return self.__class__(stream, other | self.flag)
        elif isinstance(other, stringstream):
            return other.__rlshift__(self)
        else:
            if self.flag.check(Flag.roundFloat):
                if isinstance(other, float):
                    self.stream.write(round(other))
                    return self
            self.stream.write(other)
            return self

poutF = coutF = ostreamFlags(sys.stdout)
