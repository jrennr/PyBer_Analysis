#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# In[5]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load
city_data_to_load = r"C:\Users\Columbia bootcamp\PyBer\Starter_Code\Resources\city_data.csv"
ride_data_to_load = r"C:\Users\Columbia bootcamp\PyBer\Starter_Code\Resources\ride_data.csv"


# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df = ride_data_to_load
# ride_data_df = pd.read_csv(ride_data_to_load)


# In[24]:


# Assuming you have already loaded 'ride_data_df' and 'city_data_df'

# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city"])

# Display the data table for preview
pyber_data_df.head()


# In[25]:


#  1. Get the total rides for each city type
total_rides_type = ride_data_df
total_rides_type = city_data_df
total_rides_type


# In[26]:


# 2. Get the total drivers for each city type
total_drivers_df = city_data_df.groupby("type").sum()["driver_count"]
print(total_drivers_df)


# In[41]:


#  3. Get the total amount of fares for each city type
total_fares_df = ride_data_df
total_fares_df = city_data_df
#total_fares_df.groupby(["Type"]).count()["city"]
total_fares_df.head()


# In[73]:


# Correct file paths using raw strings (add 'r' before the string)
city_data_to_load = r"C:\Users\Columbia bootcamp\PyBer\Starter_Code\Resources\city_data.csv"
ride_data_to_load = r"C:\Users\Columbia bootcamp\PyBer\Starter_Code\Resources\ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

# Filter data for each city type
suburban_cities_df = city_data_df[city_data_df["type"] == "Suburban"]
rural_cities_df = city_data_df[city_data_df["type"] == "Rural"]
urban_cities_df = city_data_df[city_data_df["type"] == "Urban"]
suburban_cities_df = ride_data_df[ride_data_df["fare"] == "Suburban"]
rural_cities_df = ride_data_df[ride_data_df["fare"] == "Rural"]
urban_cities_df = ride_data_df[ride_data_df["fare"] == "Urban"]




# In[82]:


# Get the average fare per ride for each city type
print("Columns in suburban_cities_df:")
print(suburban_cities_df.columns)

suburban_avg_fare = suburban_cities_df.groupby("city")["fare"].mean()
rural_avg_fare = rural_cities_df.groupby("city")["fare"].mean()
urban_avg_fare = urban_cities_df.groupby("city")["fare"].mean()  

#ride_data_to_load = pyber_data_df
average_fare = pyber_data_df
average_fare = pyber_data_df.groupby("city")["fare"].mean()
average_fare.head()


# In[93]:


# 5. Get the average fare per driver for each city type.
urban_avg_fare_per_driver = urban_cities_df["fare"].sum() / city_data_df[city_data_df["type"] == "Urban"]["driver_count"].sum()
suburban_avg_fare_per_driver = suburban_cities_df["fare"].sum() / city_data_df[city_data_df["type"] == "Suburban"]["driver_count"].sum()
rural_avg_fare_per_driver = rural_cities_df["fare"].sum() / city_data_df[city_data_df["type"] == "Rural"]["driver_count"].sum()


# In[97]:


# Create a PyBer summary DataFrame
#pyber_summary_df = pyber_data_df(columns=["Metric", "Value"])
pyber_summary_df = pd.DataFrame(columns=["Metric", "Value"])

# Calculate summary statistics for the "fare" column in pyber_data_df
fare_mean = pyber_data_df["fare"].mean()
fare_median = pyber_data_df["fare"].median()
fare_mode = pyber_data_df["fare"].mode().iloc[0]  # Mode can have multiple values, so we take the first one
fare_std_dev = pyber_data_df["fare"].std()


#fare_mean = statistics.mean(pyber_data_df["fare"])
#fare_median = statistics.median(pyber_data_df["fare"])
#fare_mode = statistics.mode(pyber_data_df["fare"])
#fare_std_dev = statistics.stdev(pyber_data_df["fare"])

# Add summary statistics to the pyber_summary_df DataFrame
pyber_summary_df = pyber_summary_df.append({"Metric": "Mean", "Value": fare_mean}, ignore_index=True)
pyber_summary_df = pyber_summary_df.append({"Metric": "Median", "Value": fare_median}, ignore_index=True)
pyber_summary_df = pyber_summary_df.append({"Metric": "Mode", "Value": fare_mode}, ignore_index=True)
pyber_summary_df = pyber_summary_df.append({"Metric": "Standard Deviation", "Value": fare_std_dev}, ignore_index=True)

# Display the pyber_summary_df DataFrame
print(pyber_summary_df)


# In[98]:


# 7. Cleaning up the DataFrame. Delete the index name¶
pyber_summary_df.index.name = None


# In[99]:


#  8. Format the columns.
#pyber_summary_df.count()
pyber_summary_df.isnull().sum()



# In[126]:


#Group the data by "type" and "date" and calculate fares
weekly_fares = pyber_data_df.groupby(["type", "date"])["fare"].sum()

#Reset the index to convert groupings into columns
weekly_fares = weekly_fares.reset_index()

#Create a pivot table with "date" as index, "type" as columns, and sum of fares as values
pivot_table = weekly_fares.pivot(index="date", columns="type", values="fare")

#Create the multiple line plot
pivot_table.plot(kind="line", figsize=(12, 6))


# label and title
plt.xlabel("Date")
plt.ylabel("Total Fare ($)")
plt.title("Total Weekly Fares by City Type")

# Add legend for city types
plt.legend(title="City Type", loc="best")

# Display plot
plt.show()


# In[15]:


# 1. Read the merged DataFrame
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)


# In[111]:


# Group by "type" and "date" &calculate sum of fares
fare_sum_by_type_date = pyber_data_df.groupby(["type", "date"])["fare"].sum()

# Create a new DF from the grouped data
fare_summary_df = pd.DataFrame(fare_sum_by_type_date)

# Make "type" and "date" columns
fare_summary_df = fare_summary_df.reset_index()

# Display the fare_summary_df Dataframe
print(fare_summary_df)



# In[112]:


# Reset the index of the DataFrame
fare_summary_df = fare_summary_df.reset_index()

# Display the fare_summary_df DataFrame with reset index
print(fare_summary_df)


# In[113]:


# Create a pivot table
pivot_table = fare_summary_df.pivot_table(index='date', columns='type', values='fare')

# Display the pivot table
print(pivot_table)


# In[114]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on '2019-01-01'to'2019-04-29'.

pivot_table = fare_summary_df.pivot_table(index='date', columns='type', values='fare')

# Display the pivot table
print(pivot_table)


# In[115]:


# Convert the "date" column to datetime datatype

df = fare_summary_df

df["date"] = pd.to_datetime(df["date"])

# Set the "date" column as the index
df.set_index("date", inplace=True)

# Display the DataFrame with the updated index
print(df)


# In[116]:


#fare_summary_df = df
print(fare_summary_df)


# In[117]:


# Resample the data by week and calculate the sum of fares
weekly_fares_df = fare_summary_df.resample('W').sum()

# Display the new DataFrame
print(weekly_fares_df)


# In[118]:


# 8. {lot the resample DataFrame using the df.plot() function. 

# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

weekly_fares = df.resample('W').sum()

# Display the new DataFrame
print(weekly_fares)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




