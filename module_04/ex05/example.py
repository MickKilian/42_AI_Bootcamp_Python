from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

# Load the dataset
loader = FileLoader()
data = loader.load('../attachments/athlete_events.csv')

# Get the medal counts for a given country (e.g., 'USA')
medals = how_many_medals_by_country(data, 'USA')

# Output the result
print(medals)
