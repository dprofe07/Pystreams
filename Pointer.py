import sys
class Pointer:
    '''
    usage:
        in interpreter:
            >>> x = Pointed() # to make handler
            >>> ptr = Pointer(x)
            >>> x = 10
            >>> print(+ptr)
            10
            >>> ptr *= 10000
            >>> print(x)
            10000
        in function:
            def f(x):
                
        
    '''
    MAX_RECURSION_OUTPUT = 2
    
    def __init__(self, value=None, vars_ = None):
        if value is None:
            self.obj_name = None
            self.vars = {}
            return
        self.vars = vars_ or vars(sys.modules['__main__'])
        ids = {}
        for name, val in self.vars.items():
            if name in ids.keys():
                raise Exception('Too more values with one id')
            ids[id(val)] = name
        if id(value) not in ids.keys():
            if isinstance(value, str):
                self.obj_name = value
            else:
                raise Exception('Not found!')
        else:
            self.obj_name = ids[id(value)]

    @staticmethod
    def nullptr():
        return Pointer()
    
    @staticmethod
    def fromName(name, vars_ = None):
        ptr = Pointer()
        ptr.vars = vars_ or vars(sys.modules['__main__'])
        ids = {}
        ptr.obj_name = name
        if name not in ptr.vars.keys():
            raise ValueError("Not found!")
        return ptr
    
    def __repr__(self, rec=1):
        if rec >= Pointer.MAX_RECURSION_OUTPUT:
            return f'<Pointer to {type(self.obj).__name__} {self.obj_name}=...>'
        try:
            if type(self.obj) == Pointer:
                return f'<Pointer to {type(self.obj).__name__} obj_name={self.obj_name!r} {self.obj_name}={self.obj.__repr__(rec + 1)}>'
            return f'<Pointer to {type(self.obj).__name__} obj_name={self.obj_name!r} {self.obj_name}={self.obj!r}>'
        except ValueError:
            return '<Null pointer>'
    @property
    def obj(self):
        if self.obj_name is None:
            raise ValueError('Can \'t get null pointer value')
        return self.vars[self.obj_name]
    
    @obj.setter
    def obj(self, new_value):
        if self.obj_name is None:
            raise ValueError('Can \'t assign null pointer value')
        self.vars[self.obj_name] = new_value

    def retarget_to_name(self, name, vars_=None):
        tmp = +self
        self.vars = vars_ or vars(sys.modules['__main__'])
        self.obj_name = name
        if name not in self.vars.keys():
            raise ValueError("Not found!")
        self *= tmp
    
    def retarget(self, value, vars_=None):
        tmp = +self
        self.vars = vars_ or vars(sys.modules['__main__'])
        ids = {}
        for name, val in self.vars.items():
            if name in ids.keys():
                raise Exception('Too more values with one id')
            ids[id(val)] = name
        if id(value) not in ids.keys():
            raise Exception('Not found!')
        else:
            self.obj_name = ids[id(value)]
        self *= tmp
    
    def __pos__(self):
        return self.obj

    def __imul__(self, other):
        self.obj = other
        return self


class Pointed:
    pass


