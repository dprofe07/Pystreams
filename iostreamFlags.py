from .istreamFlags import istreamFlags
from .ostreamFlags import ostreamFlags
from .flags import Flag
import sys

class iostreamFlags(istreamFlags, ostreamFlags):
    def __init__(self, stream_in=sys.stdin, stream_out=sys.stdout, flags = None):
        self.flag = flags or Flag()
        self.in_ = istreamFlags(stream_in, None, self.flag)
        self.out = ostreamFlags(stream_out, self.flag)
        self.__rshift__ = self.in_.__rshift__
        self.__lshift__ = self.out.__lshift__

pioF = cioF = iostreamFlags(sys.stdin, sys.stdout)
