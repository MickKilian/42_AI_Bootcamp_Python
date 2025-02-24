def youngest_fellah(df, year):
    # Filter the dataframe for the given year
    year_data = df[df['Year'] == year]
    
    # Filter the data by gender (Female 'F' and Male 'M')
    women = year_data[year_data['Sex'] == 'F']
    men = year_data[year_data['Sex'] == 'M']
    
    # Find the youngest age for women and men
    youngest_woman = women['Age'].min() if not women.empty else None
    youngest_man = men['Age'].min() if not men.empty else None
    
    # Return the dictionary with the youngest ages
    return {'f': youngest_woman, 'm': youngest_man}
