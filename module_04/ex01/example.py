from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

# Create an instance of FileLoader
loader = FileLoader()

# Load the dataset
data = loader.load('../attachments/athlete_events.csv')

# Call the function for the year 2004
result = youngest_fellah(data, 2004)

# Output the result
print(result)  # Expected output: {'f': 13.0, 'm': 14.0}
