from .istream import istream
from .ostream import ostream
from .flags import Flag
import sys

class iostream:
    def __init__(self, stream_in=sys.stdin, stream_out=sys.stdout):
        self.in_ = istream(stream_in, None)
        self.out = ostream(stream_out, None)

    def __rshift__(self, other):
        self.in_ >> other
        return self
    
    def __lshift__(self, other):
        self.out << other
        return self
    
pio = cio = iostream(sys.stdin, sys.stdout)
