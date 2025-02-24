import numpy as np
from ScrapBooker import ScrapBooker

# Initialize ScrapBooker
spb = ScrapBooker()

# Crop example
arr1 = np.arange(0, 25).reshape(5, 5)
print(spb.crop(arr1, (3, 1), (1, 0)))

# Thin example
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(spb.thin(arr2, 3, 0))

# Juxtapose example
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))

# Mosaic example
arr4 = np.array([[1, 2], [3, 4]])
print(spb.mosaic(arr4, (3, 3)))
