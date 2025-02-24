from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

# Load the dataset
loader = FileLoader()
data = loader.load('../attachments/athlete_events.csv')

# Example: Calculate the proportion of female tennis players in the 2004 Olympics
result = proportion_by_sport(data, 2004, 'Tennis', 'F')
print(result)  # Expected Output: 0.019302325581395347 (or a similar value based on the dataset)
