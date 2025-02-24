import pandas as pd

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        # Load the dataset and display its dimensions
        try:
            # Read the CSV file
            df = pd.read_csv(path)
            # Get the shape of the dataframe (rows x columns)
            rows, cols = df.shape
            # Display the message about dimensions
            print(f"Loading dataset of dimensions {rows} x {cols}")
            return df
        except Exception as e:
            # Handle the case where the file cannot be loaded
            print(f"Error loading file: {e}")
            return None

    def display(self, df, n):
        # Display the first n rows if n is positive, or the last n rows if n is negative
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(abs(n)))
        else:
            print("Invalid value for n. Please provide a non-zero integer.")
