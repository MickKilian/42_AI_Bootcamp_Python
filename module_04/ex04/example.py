from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

# Load the dataset
loader = FileLoader()
data = loader.load('../attachments/athlete_events.csv')

# Create the SpatioTemporalData object
sp = SpatioTemporalData(data)

# Example usage for the 'where' method
print(sp.where(1896))  # Output: ['Athina']
print(sp.where(2016))  # Output: ['Rio de Janeiro']

# Example usage for the 'when' method
print(sp.when('Athina'))  # Output: [2004, 1906, 1896]
print(sp.when('Paris'))   # Output: [1900, 1924]
