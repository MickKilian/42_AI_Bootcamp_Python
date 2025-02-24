from FileLoader import FileLoader

# Create an instance of FileLoader
loader = FileLoader()

# Load the dataset
data = loader.load("../attachments/athlete_events.csv")  # Adjust the path to where your CSV file is located

# Display the first 12 rows
loader.display(data, 12)