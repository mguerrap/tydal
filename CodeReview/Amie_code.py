“””Amie Code for plotting daily tidal height and investigating maxima and minima in tidal data 113016 v4”””

import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

%matplotlib inline
#Load data
<<<<<<< HEAD
data = pd.read_csv('../Data/2014_PortTownsend.csv', parse_dates=['Date Time'])#Use date time index

=======
data = pd.read_csv('../Data/2014_PortTownsend.csv', parse_dates=['Date Time'])

import plotly.plotly as py
import plotly.graph_objs as go
#Use date time index
>>>>>>> master
data_datetime = pd.DatetimeIndex(data['Date Time'])
#Edit data adding new columns
def f(data):
    #Grab tidal data and parse it out by year, month, day, hour, minute and time (hours but includes the minutes as decimals)
    data['Year'] = pd.DatetimeIndex(data['Date Time']).year
    data['Month'] = pd.DatetimeIndex(data['Date Time']).month
    data['Day'] = pd.DatetimeIndex(data['Date Time']).day
    data['Hour'] = pd.DatetimeIndex(data['Date Time']).hour
    data['Minute'] = pd.DatetimeIndex(data['Date Time']).minute
    data['Time'] =  data['Hour'] + data['Minute']/60
    return data

data1 = f(data)
<<<<<<< HEAD
data01012014 = data1[‘Date Time’, data1.loc[“2014-01-01 9:12:00":"2014-01-01 9:36:00"]
#Edit data so it only has time and water depth data-faster computing, keeping original for QC tests
data01012014_simp = data01012014[['Time','Water Level']]
data01012014_simp
#Looking for a local minimum and maxima and setting arrays for values to be entered into

min_x= []
min_y= []
max_x= []
max_y= []

for i in range(1, data01012014_simp.size):
    if (i==0)
    #do nothing-skip header
    else if((data01012014_simp[1,i]-data01012014_simp[1,i+1])>(data01012014_simp[1,i]-data01012014_simp[1,i+1])&& (data01012014_simp[1,i+1]-data01012014_simp[1,i+2])<(data01012014_simp[1,i+1]-data01012014_simp[1,i+2]):
       max_x= max_x[data01012014_simp[0,i]
       max_y= max_x[data01012014_simp[1,i]
    else if(data01012014_simp[1,i]-data01012014_simp[1,i+1])<data01012014_simp[1,i]-data01012014_simp[1,i+1])&&(data01012014_simp[1,i+1]-data01012014_simp[1,i+2])>(data01012014_simp[1,i+1]-data01012014_simp[1,i+2]):
       min_x= min_x[data01012014_simp[0,i]
       min_y= min_x[data01012014_simp[1,i]
    else():
    #do nothing
return(min_x, min_y, max_x, max_y)

=======
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
>>>>>>> master
#Plot one day of data
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(12, 6))
plt.plot(data01012014['Time'], data01012014['Water Level'])
plt.scatter(min_x, min_y, 'g')
plt.scatter(max_x, max_y, 'r')
plt.xlabel("Time (Hours)")
plt.ylabel("Water Depth based on MLLW")
ax.set_title("Port Townsend Water Level by Time showing High and Low Tide")
plt.show()
