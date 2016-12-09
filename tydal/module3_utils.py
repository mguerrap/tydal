import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as md
import requests

from netCDF4 import Dataset
from matplotlib import path


def tidal_currents(T, a1, a2, alpha):
    """Function estimates a depth averaged velocity
    for a simple tidal channel
    Inputs: T = Tide period (hours)
    a1 = tidal amplitude ocean side (m)
    a2 = tidal amplitude estuary side (m)
    alpha = a phase difference in degrees (º)
    L = channel length (m)
    H = channel depth (m)
    time = time at which to estimate the current,
    a number between 0 and 1, it corresponds to a stage in the tide
    Outputs: u_t = depth average current at several times between 0 and 4T"""
    g = 9.81
    L = 200000
    H = 200
    # pass period to seconds
    T = T*3600
    w = 2*np.pi/T
    dt = T/100
    t = np.arange(0, 4*T, dt)
    u_t = g*a1/L*1/w*np.sin(w*t)-g*a2/L*1/w*np.sin(w*t+alpha)
    return(u_t, t)


def plot_currents(T, a1, a2, alpha, N):
    """Plots results of analytical currents,
    plots a time series of u(t), and a dot
    in a specific velocity. Also plots an arrow
    showing the direction of the current and its magnitude
    Inputs: u = time series of u, created using tidal_currents.py
    t = time corresponding to that time series
    T = tidal period used
    t_single = time of location of dot"""
    [u, time] = tidal_currents(T, a1, a2, alpha)
    abs_u = np.absolute(u)
    max_u = np.amax(abs_u)
    u_single = u[N]
    t_single = time[N]
    fig, ax = plt.subplots(2, figsize={10, 4})
    # Arrow showing velocity
    ax[0].set_ylim([-0.5, 0.5])
    ax[0].set_xlim([-max_u-1, max_u+1])
    if u_single > 0:
        ax[0].arrow(0-u_single/2, 0, u_single, 0,
                    head_width=0.1, head_length=0.05, fc='g', ec='g')
        ax[0].text(0, -0.3, 'Flood', horizontalalignment='center', color='g',
                   verticalalignment='center', fontsize=14, fontweight='bold')
    else:
        ax[0].arrow(0-u_single/2, 0, u_single, 0,
                    head_width=0.1, head_length=0.05, fc='r', ec='r')
        ax[0].text(0, -0.3, 'Ebb', horizontalalignment='center', color='r',
                   verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(-max_u, 0.3, 'Ocean', horizontalalignment='center',
               verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(max_u, 0.3, 'Estuary', horizontalalignment='center',
               verticalalignment='center', fontsize=14, fontweight='bold')
    ax[0].text(0, 0.45, 'V = ' + str(round(u_single, 1)) + ' m/s',
               horizontalalignment='center', verticalalignment='center',
               fontsize=14, fontweight='bold')
    ax[0].axis('off')
    # Time Series
    ax[1].plot(time/3600, u, color='blue')
    ax[1].plot(t_single/3600, u_single, color='blue',
               marker='o', markersize=15)
    ax[1].set_xlabel('Time (hours)')
    ax[1].set_ylabel('Velocity (m/s)')
    ax[1].set_ylim([-2.5, 2.5])
    return


def ferry_data_download(URL):
    """Downloads the ADCP data from ferry
    Inputs:
    URL with the location of the ferry NetCDF file,
    must end with .ncml
    Outputs:
    An object containing the link to the ferry data """
    explanation = 'File exists'
    file_downloaded = True
    # Request if the thredds server is working, add .html to URL
    req = requests.get(URL + '.html')
    if req.status_code == 200:
        """File exists and is good for download, so write file"""
        print('File is ok')
        explanation = 'Good URL File downloaded'
        file_downloaded = True
        ferry = xr.open_dataset(URL)
    else:
        print('File not found or unavailable')
        explanation = ' File not found or unavailable'
        file_downloaded = False
    return (ferry, file_downloaded, explanation)


def ferry_data_QC(ferry, TH_abs, TH_u, TH_d):
    """Gets the variables and pass a QC to estimate final velocities
    Inputs: ferry data in an xarray DataSet, treshold for absolute
    velocities, TH for true velicities, TH for depth
    Outputs: Quality Controled ferry data in a xarra DataSet

    # QC1: make nan all Absolute velocities that are greater than 6.5 m/s """
    abs_u = ferry.eastward_absolute_water_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    abs_v = ferry.northward_absolute_water_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    abs_w = ferry.vertical_absolute_water_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    # Get bottom track velocity for reference
    # and also clean for TH in abs velocity
    east_btv = ferry.eastward_bottom_tracking_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    north_btv = ferry.northward_bottom_tracking_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    vert_btv = ferry.vertical_bottom_tracking_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    # Estimate u_true = abs_u + east_bt_v
    u_true = abs_u + east_btv
    v_true = abs_v + north_btv
    w_true = abs_w + vert_btv
    U = np.sqrt(u_true**2 + v_true**2)
    # QC2: check that u_true and v_true are less than 4 m/s
    u_true = u_true.where((u_true < TH_u) & (v_true < TH_u) & (U < TH_u))
    v_true = v_true.where((u_true < TH_u) & (v_true < TH_u) & (U < TH_u))
    w_true = w_true.where((u_true) < TH_u & (v_true < TH_u) & (U < TH_u))
    U = U.where((u_true) < TH_u & (v_true < TH_u) & (U < TH_u))
    # Add true velocity data to the dataset
    ferry['u_true'] = u_true
    ferry['v_true'] = v_true
    ferry['w_true'] = w_true
    ferry['Horizontal_speed'] = U
    # Remove first 5 rows of depth
    ferryQC = ferry.isel(depth=slice(TH_d, None))
    return(ferryQC)


def count_route_num(ferryQc):
    """ adds a variable to ferryQc dataset to mark the crossing number
         INPUTS:
             ferryQc - the xarray DataSet object with the ferry data
         OUTPUTS:
             ferryQc - xarray DataSet object with the ferry data, now with
                       the added variable, xing_num
    """
    # initialize vars
    counter = 0
    xing_num = np.empty((ferryQc.time.size), dtype=int)
    tdiff = np.diff(ferryQc.time.values)
    # Loop through all time values. Time gaps greater than 10mins indicate
    # ferry docking, and the start of a new transect
    for ii in range(1, ferryQc.time.size-1):
        if tdiff[ii] > np.timedelta64(10, 'm'):
            xing_num[ii] = -9
            counter = counter+1
        else:
            xing_num[ii] = counter
    # add to ferry structure
    ferryQc['xing_num'] = xr.DataArray(xing_num,
                                       coords=ferryQc.time.indexes,
                                       dims=['time'])
    return(ferryQc)


def plt_tide(pt_tide, time_index, start_date, end_date):
    """
        plot tidal elevations at port townsend station over a specified
        date range with a marker at a location specified by time_index
        INPUTS:
            pt_tide    - pandas DataFrame with the Port Townsend tidal
                         elevation data
            time_index - integer specifying iloc of vertical marker on plot
            start_date - string with first date of display range
            end_date   - string with last date of display range
        OUTPUTS: A matplotlib subplot with tidal elevations,
                 and a vertical marker
                 at the location specified in time_index
    """
    if pt_tide[start_date:end_date].size < time_index:
        raise ValueError('time_index out of specified date range')
    # sub_selected time for vertical bar, as chosen by time_index
    time = pt_tide[start_date:end_date].index[time_index]
    # note conversion to meters
    plt.plot(pt_tide[start_date:end_date]*0.3048)
    max = 3.5
    min = -0.5
    plt.hold('True')
    # plot vertical line at location specified in time
    plt.plot([time, time], [min, max])
    # Clean up and label axes
    plt.ylabel('Elevation [m]')
    plt.gca().xaxis.tick_top()


def plt_ferry_and_tide(ferryQc, pt_tide, crossing_index, start_date, end_date):
    """ plots Port Townsend tidal elevations and ferry crossing data on two
        subplots.
        INPUTS
            ferryQc:     xarray data set with quality controlled ferry data
            pt_tide:     port townsend tidal elevations as a pandas DataFrame
            cross_index: integer of ferry crossing to be displayed
            start_date:  start of tidal elevation time series to be plotted
            end_date:    end of tidal elevation time series to be plotted
        OUTPUTS
            Figure with two subplots
    """
    # subsample ferryQc Data
    ferry_subsample = ferryQc.sel(time=slice(start_date, end_date))
    min_xing = min(ferry_subsample.xing_num
                   [ferry_subsample.xing_num != -9].values)
    max_xing = max(ferry_subsample.xing_num
                   [ferry_subsample.xing_num != -9].values)
    valid_xings = np.arange(min_xing, max_xing, 2)
    # check cross_index is in range
    if (crossing_index > valid_xings.size):
        print('Invalid Ferry Xing index')
        print(str(valid_xings.size) + ' number of crossings ' +
              'for the chosen date range')
        return
    chosen_xing_num = valid_xings[crossing_index]
    # find indexing for both datasets
    ferry_time_index = ferry_subsample['time'].to_index()
    pt_time_index = pt_tide[start_date:end_date].index
    # find crossing that matches time_index
    mid_ferry_time = ferry_time_index[np.where(
                     ferry_subsample.xing_num == chosen_xing_num)]
    mid_ferry_time = mid_ferry_time[int(mid_ferry_time.size/2)]
    # find numeric index in the pt_tides DataFrame that matches
    # the nearest in the ferry data
    pt_time_val = pt_time_index.searchsorted(mid_ferry_time)
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize={10, 4})
    # plot tidal elevations
    plt.sca(axes[0])
    plt_tide(pt_tide, pt_time_val, start_date, end_date)
    plt.gca().xaxis.tick_top()
    # Ferry Plots
    plt.sca(axes[1])
    plt_index = ferry_subsample.xing_num.values == chosen_xing_num
    # Check for existing values in array
    if not np.all(np.isnan(
                  ferry_subsample.Horizontal_speed[plt_index].values)):
        ferry_subsample.Horizontal_speed[plt_index].plot(x='time', y='depth')
    else:
        print('All NaN speed values')
    # plot bottom track
    ferry_subsample.bottom_tracking_depth_beam_1[plt_index].plot()
    # format axes
    plt.gca().invert_yaxis()
    plt.ylabel('Depth [m]')
    plt.clim(0, 3)
    # format xticks
    xfmt = md.DateFormatter('%m-%d %H:%M')
    axes[1].xaxis.set_major_formatter(xfmt)
    return
