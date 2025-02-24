import pandas as pd

def proportion_by_sport(data, year, sport, gender):
    # Filter the dataset by the given year and gender
    filtered_data = data[(data['Year'] == year) & (data['Sex'] == gender)]
    
    # Drop duplicates based on the athlete's ID (ensure each athlete is counted only once)
    unique_participants = filtered_data.drop_duplicates(subset='ID')
    
    # Filter the data to get the participants who played the specified sport
    sport_participants = unique_participants[unique_participants['Sport'] == sport]
    
    # Calculate the proportion
    total_participants = len(unique_participants)
    sport_participants_count = len(sport_participants)
    
    # If there are no participants of the given gender in the given year, return 0
    if total_participants == 0:
        return 0.0
    
    proportion = sport_participants_count / total_participants
    return proportion
