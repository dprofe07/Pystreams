from .ostreamFlags import ostreamFlags, sys
from .flags import Flag
class ostream(ostreamFlags):
    def __init__(self, stream=sys.stdout, flag=None):
        super().__init__(stream)
    def __lshift__(self, other):
        if isinstance(other, Flag):
            self.stream.write(other)
            return self
        else:
            return super().__lshift__(other)

pout = cout = ostream(sys.stdout)
