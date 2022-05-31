from .flags import Flag
from .stringstream import stringstream
from .special import returner, toBuffer
from classes.Pointer import Pointer
import sys


class istreamFlags:
    _buffer = []

    def __init__(self, stream=sys.stdin, tip=None, flag=None):
        self.stream = stream
        self.type = tip if callable(tip) else (lambda x: x)
        self.flag = flag or Flag()

    def __rshift__(self, other):
        if callable(other):
            return self.__class__(self.stream, other, self.flag)

        elif isinstance(other, Flag):
            return self.__class__(self.stream, self.type, other | self.flag)

        elif isinstance(other, stringstream):
            return other.__rrshift__(self)

        elif other == returner:
            while not self._buffer:
                self._buffer += self.stream.readline().split()
            return self.type(self._buffer.pop(0))

        elif other == toBuffer:
            self._buffer += self.stream.readline().split()
            return self

        elif isinstance(other, str) and self.flag.check(Flag.fromStringName):
            if self.flag.check(Flag.fromBuffer) and not self.getBuffer():
                raise ValueError('Buffer is empty')
            while not self._buffer:
                self._buffer += self.stream.readline().split()

            ptr = Pointer.fromName(other)

            return self >> ptr

        elif isinstance(other, Pointer):
            if self.flag.check(Flag.fromBuffer) and not self.getBuffer():
                raise ValueError('Buffer is empty')
            while not self._buffer:
                self._buffer += self.stream.readline().split()
            other.obj = self.type(self._buffer.pop(0))
            return self

        else:
            try:
                ptr = Pointer(other)
            except:
                pass
            else:
                return self >> ptr
            raise TypeError('value must be Pointer to value or string name of value')



    def flush(self):
        self._buffer.clear()

    def getBuffer(self):
        return self._buffer.copy()


pinF = cinF = istreamFlags(sys.stdin)
