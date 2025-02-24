from FileLoader import FileLoader
from HowManyMedals import how_many_medals

# Load the dataset
loader = FileLoader()
data = loader.load('../attachments/athlete_events.csv')

# Call the function for a specific participant
result = how_many_medals(data, 'Kjetil Andr Aamodt')

# Output the result
print(result)
