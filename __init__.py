from .istream import pin, cin, istream
from .ostream import pout, cout, ostream
from .stringstream import stringstream
from .iostream import pio, cio, iostream
from .istreamFlags import pinF, cinF, istreamFlags
from .ostreamFlags import poutF, coutF, ostreamFlags
from .stringstreamFlags import stringstreamFlags
from .iostreamFlags import pioF, cioF, iostreamFlags
from .flags import Flag, DissableFlag
from .special import toBuffer, returner


if __name__=='__main__':
    pout << "Hello, world!\n"
    pout << "Enter your name there(Name & Surname): "
    pin >> str >> toBuffer
    FI = stringstream()
    pin >> FI
    name = FI >> returner
    FI << " " << name
    pout << "Hello, " << FI
    del name, FI

__ALL__ = [
    'pin', 'cin',
    'pout', 'cout',
    'stringstream',
    'pio', 'cio',
    'pinF', 'cinF',
    'poutF', 'coutF',
    'Flag', 'DissableFlag',
    'stringstreamFlags',
    'SpecialFunction',
    'toBuffer', 'returner',
]
