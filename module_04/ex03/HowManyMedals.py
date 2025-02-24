def how_many_medals(df, name):
    # Filter the dataframe for the given participant's name
    athlete_data = df[df['Name'] == name]
    
    # Initialize a dictionary to store the results
    medals_by_year = {}
    
    # Group by 'Year' and 'Medal', and count the occurrences of each medal type for each year
    for year in athlete_data['Year'].unique():
        # Filter the data for this specific year
        year_data = athlete_data[athlete_data['Year'] == year]
        
        # Initialize medal counts for this year
        medal_counts = {'G': 0, 'S': 0, 'B': 0}
        
        # Count the medals of each type ('G', 'S', 'B')
        for medal in year_data['Medal']:
            if medal == 'Gold':
                medal_counts['G'] += 1
            elif medal == 'Silver':
                medal_counts['S'] += 1
            elif medal == 'Bronze':
                medal_counts['B'] += 1
        
        # Add the medal counts to the result dictionary
        medals_by_year[year] = medal_counts
    
    return medals_by_year
