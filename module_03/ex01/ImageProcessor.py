import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

class ImageProcessor:
    def load(self, path):
        try:
            # Attempt to load the image using matplotlib
            img = mpimg.imread(path)
            
            # Display the image dimensions
            print(f"Loading image of dimensions {img.shape[0]} x {img.shape[1]}")
            
            return img
        
        except FileNotFoundError as e:
            # Handle case where the file is not found
            print(f"Exception: FileNotFoundError -- {e.strerror}: {path}")
            return None
        
        except OSError as e:
            # Handle case where the file can't be read as an image
            print(f"Exception: OSError -- {e.strerror}")
            return None
        
    def display(self, array):
        if array is None:
            print("No image to display.")
            return
        
        # Display the image using matplotlib
        plt.imshow(array)
        plt.axis('off')  # Hide axes
        plt.show()

# Example usage:
if __name__ == "__main__":
    imp = ImageProcessor()
    
    # Testing the load method
    arr = imp.load("non_existing_file.png")  # Test case: non-existing file
    print(arr)  # Output: None
    
    arr = imp.load("empty_file.png")  # Test case: empty file (not a valid image)
    print(arr)  # Output: None
    
    arr = imp.load("../attachments/42AI.png")  # Test case: valid image path
    print(arr)  # Output: The image array (numpy array of shape (height, width, 3))
    
    imp.display(arr)  # Display the image
