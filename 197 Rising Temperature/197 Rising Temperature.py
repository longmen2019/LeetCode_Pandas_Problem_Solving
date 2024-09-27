import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by 'recordDate'
    weather.sort_values('recordDate', inplace=True)

    # Calculate differences in temperature and recordDate
    temp_diff = weather['temperature'].diff()
    date_diff = weather['recordDate'].diff()

    # Filter rows where temperature is higher than the previous day
    # and the date difference is exactly 1 day
    high_temp_id = weather[(temp_diff > 0) & (date_diff == pd.Timedelta(days=1))]
    return pd.DataFrame(high_temp_id['id'])

data = {
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
}

weather_df = pd.DataFrame(data)
print(weather_df)
print(" ")

# converts the recordDate column in the weather_df DataFrame from a string format to a datetime format
weather_df['recordDate'] = pd.to_datetime(weather_df['recordDate'])
print(rising_temperature(weather_df))
