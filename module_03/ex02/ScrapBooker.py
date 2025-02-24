import numpy as np

class ScrapBooker:
    
    def crop(self, array, dim, position=(0,0)):
        height, width = dim
        start_x, start_y = position

        if start_x + height > array.shape[0] or start_y + width > array.shape[1]:
            return None
        
        return array[start_x:start_x+height, start_y:start_y+width]

    def thin(self, array, n, axis):
        if axis == 0:  # Vertical (remove rows)
            if n > array.shape[0]:
                return None
            new_arr = array[::n, :]
        elif axis == 1:  # Horizontal (remove columns)
            if n > array.shape[1]:
                return None
            new_arr = array[:, ::n]
        else:
            return None
        return new_arr

    def juxtapose(self, array, n, axis):
        if axis == 0:  # Vertical (stack images vertically)
            new_arr = np.vstack([array] * n)
        elif axis == 1:  # Horizontal (stack images horizontally)
            new_arr = np.hstack([array] * n)
        else:
            return None
        return new_arr

    def mosaic(self, array, dim):
        height, width = dim
        new_arr = np.tile(array, (height, width))
        return new_arr
