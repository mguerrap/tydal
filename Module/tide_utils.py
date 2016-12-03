import os
import glob
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt


def load_Neah_Bay(datadir):
    """
    Function to load the Neah Bay tidal station data from 2015 - 2016
    and returns a dataframe and a Datetime Index object
    Datadir is the directory path to where the data is located
    """
    if not glob.glob(os.path.join(datadir, '*NeahBay.csv')):
        return None
    else:
        NeahBay_2014 = pd.read_csv(datadir + "2014_NeahBay.csv",
                                   parse_dates=['Date Time'],
                                   index_col=['Date Time'])
        NeahBay_2015 = pd.read_csv(datadir + "2015_NeahBay.csv",
                                   parse_dates=['Date Time'],
                                   index_col=['Date Time'])
        NeahBay_2016 = pd.read_csv(datadir + "2016_NeahBay.csv",
                                   parse_dates=['Date Time'],
                                   index_col=['Date Time'])
        NeahBay = NeahBay_2014.append(NeahBay_2015)
        NeahBay = NeahBay.append(NeahBay_2016)
        NeahBay.index.rename('datetime', inplace=True)
        return NeahBay


def load_Port_Townsend(datadir):
    """
    Function to load the Port Townsend tidal station data from 2015
    & 2016. Supply the directory to where the csv files with the
    data are saved. Returns None if files are not located in
    specified directory.
    """
    if not glob.glob(os.path.join(datadir, '*PortTownsend.csv')):
        return None
    else:
        PortTownsend_2014 = pd.read_csv(datadir +
                                        '2014_PortTownsend.csv',
                                        parse_dates=['Date Time'],
                                        index_col=['Date Time'])
        PortTownsend_2015 = pd.read_csv(datadir +
                                        '2015_PortTownsend.csv',
                                        parse_dates=['Date Time'],
                                        index_col=['Date Time'])
        PortTownsend_2016 = pd.read_csv(datadir +
                                        '2016_PortTownsend.csv',
                                        parse_dates=['Date Time'],
                                        index_col=['Date Time'])
        PortTownsend = PortTownsend_2014.append(PortTownsend_2015)
        PortTownsend = PortTownsend.append(PortTownsend_2016)
        PortTownsend.index.rename('datetime', inplace=True)
        return PortTownsend


def load_Port_Angeles(datadir):
    """
    Function to load the Port Angeles tidal station data from 2015
    & 2016. Supply the directory to where the csv files with the
    data are saved. Returns None if files are not located in
    specified directory.
    """
    if not glob.glob(os.path.join(datadir, '*PortAngeles.csv')):
        return None
    else:
        # Load the Port Angeles tidal data and put into one dataframe
        PortAngeles_2014 = pd.read_csv(datadir +
                                       '2014_PortAngeles.csv',
                                       parse_dates=['Date Time'],
                                       index_col=['Date Time'])
        PortAngeles_2015 = pd.read_csv(datadir +
                                       '2015_PortAngeles.csv',
                                       parse_dates=['Date Time'],
                                       index_col=['Date Time'])
        PortAngeles_2016 = pd.read_csv(datadir +
                                       '2016_PortAngeles.csv',
                                       parse_dates=['Date Time'],
                                       index_col=['Date Time'])
        PortAngeles = PortAngeles_2014.append(PortAngeles_2015)
        PortAngeles = PortAngeles.append(PortAngeles_2016)
        PortAngeles.index.rename('datetime', inplace=True)
        return PortAngeles


def load_tide_data(datadir):
    """
    Upper level load function for the Tide Data.
    Datadir is the directory where the data .csv files are saved
    """
    NeahBay = load_Neah_Bay(datadir)
    PortAngeles = load_Port_Angeles(datadir)
    PortTownsend = load_Port_Townsend(datadir)
    if NeahBay is None:
        return None
    elif PortAngeles is None:
        return None
    elif PortTownsend is None:
        return None
    else:
        return NeahBay, PortAngeles, PortTownsend


def create_tide_dataset(NeahBay, PortAngeles, PortTownsend):
    """
    Function takes in the tidal station dataframes and returns
    an Xarray Dataset with the tidal station data
    """
    NB = xr.DataArray(NeahBay['Water Level'], dims='datetime')
    PA = xr.DataArray(PortAngeles['Water Level'], dims='datetime')
    PT = xr.DataArray(PortTownsend['Water Level'], dims='datetime')
    Tides = xr.Dataset({'NeahBay': NB, 'PortAngeles': PA,
                       'PortTownsend': PT})
    return Tides


def plot_tide_data(Tides,time1,time2):
    """
    Function that allows to pass through variables to
    the interactive widget.
    Inputs:
        Tides - Xarray DataSet with the tidal station data
        time1 - start time to slice the tidal data
        time2 - end time to slice the tidal data
    """
    from ipywidgets import interact
    import ipywidgets as widgets

    NB = Tides.NeahBay.sel(datetime=slice(time1,time2))
    PA = Tides.PortAngeles.sel(datetime=slice(time1,time2))
    PT = Tides.PortTownsend.sel(datetime=slice(time1,time2))

    slide = widgets.IntSlider(1,1,len(NB.datetime.values)-1)
    interact(plot_tide_time_series,NB=widgets.fixed(NB),
             PA=widgets.fixed(PA),PT=widgets.fixed(PT),dt=slide)


def plot_tidal_elevation(NB,PA,PT,dt):
    """
    Function to plot the tidal elevation taken from
    the function plot_tide_data interactive slider
    """
    try:
        fig, axes = plt.subplots(nrows=1, ncols=1)
        # Get each station's tidal elevation based 
        # on the widget slider
        NBelev = NB.values[dt.values]
        PAelev = PA.values[dt.values]
        PTelev = PT.values[dt.values]
        # Create dummy x-values
        x = (1, 2, 3)
        y = (NBelev, PAelev, PTelev)
        # Create the figure with station labels
        axes.scatter(x, y, s=100, color="red", zorder=2)
        axes.plot(x, y, 'b', zorder=1)
        axes.xticks(x, ['Neah Bay', 'Port Angeles', 'Port Townsend'],
                   rotation='vertical')
        axes.grid()
        axes.ylabel('Tidal Elevation (m)')
    except:
        return None


def plot_tide_time_series(NB,PA,PT,dt):
    """
    This function plots the three tidal stations for the given
    time period along with a marker showing the time and elevation
    selected using the widget slider
    Input:
        NB - Neah Bay tide DataArray
        PA - Port Angeles tide DataArray
        PT - Port Townsend tide DataArray
    """
    import tide_utils as tide
    fig, axes = plt.subplots(nrows=3)
    NB.plot(ax=axes[0])
    axes[0].scatter(x=NB.datetime.values[dt], y=NB.values[dt],
                    color="red", s=100)
    axes[0].grid()

    PA.plot(ax=axes[1])
    axes[1].scatter(x=NB.datetime.values[dt], y=PA.values[dt],
                    color="red", s=100)
    axes[1].grid()

    PT.plot(ax=axes[2])
    axes[2].scatter(x=NB.datetime.values[dt], y=PT.values[dt],
                    color="red", s=100)
    axes[2].grid()
    
    plot_tidal_elevation(NB,PA,PT,dt)





