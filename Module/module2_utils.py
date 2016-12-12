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
    try:
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
    except FileNotFoundError:
        return None


def load_Port_Townsend(datadir):
    """
    Function to load the Port Townsend tidal station data from 2015
    & 2016. Supply the directory to where the csv files with the
    data are saved. Returns None if files are not located in
    specified directory.
    """
    try:
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
    except FileNotFoundError:
        return None


def load_Port_Angeles(datadir):
    """
    Function to load the Port Angeles tidal station data from 2015
    & 2016. Supply the directory to where the csv files with the
    data are saved. Returns None if files are not located in
    specified directory.
    """
    try:
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
    except:
        return None


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
    try:
        NB = xr.DataArray(NeahBay['Water Level'], dims='datetime')
        PA = xr.DataArray(PortAngeles['Water Level'], dims='datetime')
        PT = xr.DataArray(PortTownsend['Water Level'], dims='datetime')
        Tides = xr.Dataset({'NeahBay': NB, 'PortAngeles': PA,
                           'PortTownsend': PT})
        return Tides
    except:
        return None


def plot_tide_data(Tides, time1, time2):
    """
    Function that allows to pass through variables to
    the interactive widget.
    Inputs:
        Tides - Xarray DataSet with the tidal station data
        time1 - start time to slice the tidal data
        time2 - end time to slice the tidal data
    """
    import numpy as np
    import pandas as pd
    t1 = np.datetime64(pd.to_datetime(time1))
    t2 = np.datetime64(pd.to_datetime(time2))
    tmin = np.datetime64(Tides.datetime.values.min())
    tmax = np.datetime64(Tides.datetime.values.max())
    if t2 < tmin:
        raise IndexError('Selected times are below available range.')
    elif t1 > tmax:
        raise IndexError('Selected times are above available range.')
    elif t1 > t2:
        raise IndexError('End time occurs before start time.')
    else:
        try:
            from ipywidgets import interact
            import ipywidgets as widgets

            NB = Tides.NeahBay.sel(datetime=slice(time1, time2))
            PA = Tides.PortAngeles.sel(datetime=slice(time1, time2))
            PT = Tides.PortTownsend.sel(datetime=slice(time1, time2))

            slide = widgets.IntSlider(1, 1,
                                      len(NB.datetime.values)-1)
            interact(plot_tide_time_series, NB=widgets.fixed(NB),
                     PA=widgets.fixed(PA), PT=widgets.fixed(PT),
                     dt=slide)
        except ImportError:
            raise ImportError("Please install ipywidgets")


def plot_tidal_elevation(NB, PA, PT, slide):
    try:
        # Create a figure with 3 rows & 1 column
        fig, axes = plt.subplots(nrows=1, ncols=1)
        # Get each station's tidal elevation based on the widget slider
        NBelev = NB.values[slide]
        PAelev = PA.values[slide]
        PTelev = PT.values[slide]
        # Create dummy x-values
        x = (1, 2, 3)
        y = (NBelev, PAelev, PTelev)
        # Create the figure with station labels
        plt.scatter(x, y, s=100, color="red", zorder=2)
        plt.plot(x, y, 'b', zorder=1)
        plt.xticks(x, ['Neah Bay', 'Port Angeles', 'Port Townsend'],
                   rotation='vertical')
        plt.grid()
        plt.ylabel('Tidal Elevation (m)')
    except:
        return None


def plot_tide_time_series(NB, PA, PT, dt):
    """
    This function plots the three tidal stations for the given
    time period along with a marker showing the time and elevation
    selected using the widget slider
    Input:
        NB - Neah Bay tide DataArray
        PA - Port Angeles tide DataArray
        PT - Port Townsend tide DataArray
    """
    try:
        fig, axes = plt.subplots(nrows=3)
        NB.plot(ax=axes[0])
        axes[0].scatter(x=NB.datetime.values[dt], y=NB.values[dt],
                        color="red", s=100)
        axes[0].grid()
        axes[0].set_title('Tidal Elevation (m)')

        PA.plot(ax=axes[1])
        axes[1].scatter(x=NB.datetime.values[dt], y=PA.values[dt],
                        color="red", s=100)
        axes[1].grid()

        PT.plot(ax=axes[2])
        axes[2].scatter(x=NB.datetime.values[dt], y=PT.values[dt],
                        color="red", s=100)
        axes[2].grid()

        plot_tidal_elevation(NB, PA, PT, dt)
    except:
        return None


def add_station_maps(API='AIzaSyASHzuwtrEHNRuadF-MhNbARUnSyFfRA9Q'):
    """
    This function displays a google map of the
    locations of the three stations with the
    tidal data
    """
    # Put in the locations of the tidal stations
    NB = [48 + 22.2/60, -(124 + 36.1/60)]
    PA = [48 + 7.5/60, -(123 + 26.5/60)]
    PT = [48 + 6.8/60, -(122 + 45.6/60)]
    latlon = [tuple(NB), tuple(PA), tuple(PT)]
    # Generate the google map
    try:
        import gmaps
        gmaps.configure(api_key=API)
        m = gmaps.Map()
        markers = gmaps.marker_layer(latlon)
        m.add_layer(markers)
        return m
    except ImportError:
        raise ImportError('Please install gmaps package')
    else:
        return None
