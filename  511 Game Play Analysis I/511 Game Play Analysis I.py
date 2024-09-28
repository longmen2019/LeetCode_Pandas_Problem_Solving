import pandas as pd

# Sample data

data = {
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
    'games_played': [5, 6, 1, 0, 5]
}

# Create DataFrame
activity = pd.DataFrame(data)

# Convert event_date to datetime
activity['event_date'] = pd.to_datetime(activity['event_date'])

# Find the first login date for each player
result = activity.groupby('player_id')['event_date'].min().reset_index()
# activity.groupby('player_id'): this part of the code groups the DataFrame activity by the player_id column.
# Grouping means that all rows with the same player_id are collected together.
# After grouping by player_id, we select the event_date column from each group.
# This means we are focusing on the event_date values within each group of player_id
# The .min() function is then applied to the event_date column within each group.
# This function calculates the minimum value of event_date for each player_id group, which corresponds to the earliest login date for each player
# Finally, .reset_index() is used to convert the resulting Series back into a DataFrame.
# By default, the groupby operation results in a Series with player_id as the index.
# reset_index() moves player_id back to a regular column and resets the index to the default integer index

result.columns =['player_id', 'event_date']
print(result)