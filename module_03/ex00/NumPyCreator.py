import numpy as np

class NumPyCreator:
    
    def from_list(self, lst, dtype=None):
        try:
            return np.array(lst, dtype=dtype)
        except:
            return None
    
    def from_tuple(self, tpl, dtype=None):
        try:
            return np.array(tpl, dtype=dtype)
        except:
            return None

    def from_iterable(self, itr, dtype=None):
        return np.array(itr, dtype=dtype)
    
    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype=dtype)
    
    def random(self, shape):
        return np.random.random(shape)
    
    def identity(self, n):
        return np.eye(n)
