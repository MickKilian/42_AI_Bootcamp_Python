class SpatioTemporalData:
    def __init__(self, df):
        # Store the dataset in the instance
        self.df = df

    def when(self, location):
        # Return a list of years when the games were held in the given location
        years = self.df[self.df['City'] == location]['Year'].unique().tolist()
        return sorted(years)

    def where(self, year):
        # Return a list of locations where the games were held in the given year
        locations = self.df[self.df['Year'] == year]['City'].unique().tolist()
        return locations
