
class Flag:
    def __init__(self, *names):
        self.names = set(names)
    def __or__(self, other):
        return Flag(*self.names, *other.names)
    def check(self, flag):
        f = True
        for i in flag.names:
            f &= i in self.names
        return f
class DissableFlag(Flag):
    def __or__(self, other):
        return Flag(*(other.names - self.names))

_flags = ['fromBuffer', 'roundFloat', 'flusher', 'fromStringName']

for i in _flags:
    setattr(Flag, i, Flag(i))
    setattr(DissableFlag, i, DissableFlag(i))

