import numpy as np

class ColorFilter:
    
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        """
        return 255 - array.copy()  # Inverts colors by subtracting from 255
    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        """
        shape = array.shape
        blue_image = np.zeros(shape, dtype=array.dtype)
        blue_image[..., 2] = array[..., 2]  # Only keep blue channel (index 2)
        return blue_image
    
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        """
        green_image = array.copy()
        green_image[..., 0] = 0  # Set red channel to 0
        green_image[..., 2] = 0  # Set blue channel to 0
        return green_image
    
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        """
        red_image = array.copy()
        red_image[..., 1] = 0  # Set green channel to 0
        red_image[..., 2] = 0  # Set blue channel to 0
        return red_image
    
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        """
        # Create thresholds for shades of the image
        thresholds = np.linspace(0, 255, 5)
        shades = np.dstack([np.digitize(array[..., i], thresholds) for i in range(3)])
        # Scale the shades back to the 0-255 range
        return np.minimum(shades, 255)
    
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        """
        if filter in ['m', 'mean']:
            # Mean of R, G, and B channels
            return np.mean(array, axis=2).astype(array.dtype)
        
        elif filter in ['w', 'weight']:
            r_weight = kwargs.get('r_weight', 0.33)
            g_weight = kwargs.get('g_weight', 0.33)
            b_weight = kwargs.get('b_weight', 0.34)
            # Weighted mean of R, G, and B channels
            return (r_weight * array[..., 0] + g_weight * array[..., 1] + b_weight * array[..., 2]).astype(array.dtype)
        
        return None
