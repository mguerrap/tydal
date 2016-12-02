#Amie Code for plotting a daily value and investigating data
#112016 v3

import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline
#Load data
data = pd.read_csv('../Data/2014_PortTownsend.csv', parse_dates=['Date Time'])

import plotly.plotly as py
import plotly.graph_objs as go
#Use date time index
data_datetime = pd.DatetimeIndex(data['Date Time'])
#Edit data adding new columns
def f(data):
    data = data.copy()
    data['Year'] = pd.DatetimeIndex(data['Date Time']).year
    data['Month'] = pd.DatetimeIndex(data['Date Time']).month
    data['Day'] = pd.DatetimeIndex(data['Date Time']).day
    data['Hour'] = pd.DatetimeIndex(data['Date Time']).hour
    data['Minute'] = pd.DatetimeIndex(data['Date Time']).minute
    data['Time'] =  data['Hour'] + data['Minute']/60
    return data

data1 = f(data)
#Only grab 2014 data
data2014 = data1.query('Year == 2014')
#Only grab January data
data012014 = data2014.query('Month == 1')
#Only grab January first data
data01012014 = data012014.query('Day == 1')
#Edit data si it only has time and water depth data
data01012014_simp = data01012014[['Time','Water Level']]
data01012014_simp
#Look fo local miniums and maxs
data01012014_simp.sort_values(by=['Water Level', 'Time'], ascending=True)
#Looking for a local minimum
data01012014_simp[(data01012014_simp.Time >= 15) & (data01012014_simp.Time <= 20)]
#Plot one day of data
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(12, 6))
plt.plot(data01012014['Time'], data01012014['Water Level'])
plt.scatter(22.8, 9.5)
plt.xlabel("Time (H)")
plt.ylabel("Water Depth based on MLLW")
ax.set_title("Port Townsend Water Level by Time showing High and Low Tide")
plt.show()
