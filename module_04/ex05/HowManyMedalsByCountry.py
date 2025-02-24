def how_many_medals_by_country(df, country):
    # Define the list of team sports where we should avoid counting duplicated medals
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing',
                   'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                   'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']

    # Filter the dataset for the given country and where a medal was won
    df_country = df[(df['NOC'] == country) & (df['Medal'].notna())]

    # Initialize a dictionary to store the medal counts
    medal_counts = {}

    # Iterate over the rows of the filtered dataset
    for _, row in df_country.iterrows():
        year = row['Year']
        medal = row['Medal']
        sport = row['Sport']

        # Initialize the year dictionary if it does not exist
        if year not in medal_counts:
            medal_counts[year] = {'G': 0, 'S': 0, 'B': 0}

        # If the sport is in the team_sports list, we count only one medal per team event
        if sport in team_sports:
            # Check if this medal type has already been counted for the country in this year
            if medal == 'Gold' and medal_counts[year]['G'] == 0:
                medal_counts[year]['G'] += 1
            elif medal == 'Silver' and medal_counts[year]['S'] == 0:
                medal_counts[year]['S'] += 1
            elif medal == 'Bronze' and medal_counts[year]['B'] == 0:
                medal_counts[year]['B'] += 1
        else:
            # For individual sports, count every medal
            if medal == 'Gold':
                medal_counts[year]['G'] += 1
            elif medal == 'Silver':
                medal_counts[year]['S'] += 1
            elif medal == 'Bronze':
                medal_counts[year]['B'] += 1

    return medal_counts
