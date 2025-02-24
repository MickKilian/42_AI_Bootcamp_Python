from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

# Load the dataset
loader = FileLoader()
data = loader.load('../attachments/athlete_events.csv')

# Example of using the histogram method
MyPlotLib.histogram(data, ['Age', 'Height', 'Weight'])

# Example of using the density method
MyPlotLib.density(data, ['Age', 'Height', 'Weight'])

# Example of using the pair plot method
MyPlotLib.pair_plot(data, ['Age', 'Height', 'Weight'])

# Example of using the box plot method
MyPlotLib.box_plot(data, ['Age', 'Height', 'Weight'])
