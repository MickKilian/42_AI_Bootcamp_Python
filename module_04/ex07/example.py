# Import necessary classes
from Komparator import Komparator  # Import Komparator class
from FileLoader import FileLoader  # Import FileLoader class

# Load the dataset
loader = FileLoader()  # Instantiate the loader
data = loader.load('../attachments/athlete_events.csv')  # Make sure the path is correct

# Create an instance of the Komparator class
komparator = Komparator(data)

# Example usage of the Komparator methods
komparator.compare_box_plots('Sex', 'Height')  # Compare box plots of height by sex
komparator.density('Sex', 'Height')  # Plot density of height by sex
komparator.compare_histograms('Sex', 'Age')  # Compare histograms of age by sex
