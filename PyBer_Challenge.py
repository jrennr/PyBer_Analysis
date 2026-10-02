from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

data_dir = Path.cwd()
city_data_df = pd.read_csv(data_dir / 'city_data.csv')
ride_data_df = pd.read_csv(data_dir / 'ride_data.csv', parse_dates=['date'])
pyber_data_df = ride_data_df.merge(city_data_df, on='city', how='left', validate='many_to_one')
if pyber_data_df['type'].isna().any():
    raise ValueError('Every ride must have a matching city.')
pyber_data_df.head()

total_rides = pyber_data_df.groupby('type')['ride_id'].count()
total_drivers = city_data_df.groupby('type')['driver_count'].sum()
total_fares = pyber_data_df.groupby('type')['fare'].sum()
pyber_summary_df = pd.DataFrame({
    'Total Rides': total_rides,
    'Total Drivers': total_drivers,
    'Total Fares': total_fares,
    'Average Fare per Ride': total_fares.div(total_rides.replace(0, float('nan'))),
    'Average Fare per Driver': total_fares.div(total_drivers.replace(0, float('nan')))
})
pyber_summary_df.index.name = None
print(pyber_summary_df)

fare_summary_df = pyber_data_df.groupby(['date', 'type'])['fare'].sum().unstack('type').fillna(0)
weekly_fares_df = fare_summary_df.loc['2019-01-01':'2019-04-29'].resample('W').sum()
with plt.style.context('fivethirtyeight'):
    ax = weekly_fares_df.plot(figsize=(12, 6))
    ax.set(title='Total Weekly Fares by City Type', xlabel='Date', ylabel='Total Fare ($)')
    ax.legend(title='City Type')
    plt.tight_layout()
    plt.show()
