import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as md


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

        OUTPUTS: A matplotlib subplot with tidal elevations, and a vertical marker
                 at the location specified in time_index
    """
    
    #sub_selected time for vertical bar, as chosen by time_index
    time = pt_tide[start_date:end_date].index[time_index];
    
    #note conversion to meters
    plt.plot( pt_tide[start_date:end_date]*0.3048 );
    max = 3.5;
    min = -0.5;
    plt.hold('True')

    #plot vertical line at location specified in time
    plt.plot([time, time], [min, max] )
    
    #Clean up and label axes
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
    
    #subsample ferryQc Data
    ferry_subsample = ferryQc.sel(time=slice(start_date, end_date))
    
    min_xing = min( ferry_subsample.xing_num[ferry_subsample.xing_num != -9].values  )
    max_xing = max( ferry_subsample.xing_num[ferry_subsample.xing_num != -9].values  )
    valid_xings = np.arange(min_xing, max_xing, 2)
    
    #check cross_index is in range
    if (crossing_index > valid_xings.size):
        print('Invalid Ferry Xing index')
        print(str(valid_xings.size) +' number of crossings for the chosen date range')
        return
    
    chosen_xing_num = valid_xings[crossing_index];
    #find indexing for both datasets
    ferry_time_index = ferry_subsample['time'].to_index()
    pt_time_index = pt_tide[start_date:end_date].index;
    
    #find crossing that matches time_index
    mid_ferry_time = ferry_time_index[np.where(ferry_subsample.xing_num == chosen_xing_num)]
    mid_ferry_time = mid_ferry_time[int(mid_ferry_time.size/2)]
    
    #find numeric index in the pt_tides DataFrame that matches the nearest in the
    #   ferry data
    pt_time_val = pt_time_index.searchsorted( mid_ferry_time )
    
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize={10, 4})
    #plot tidal elevations 

    plt.sca(axes[0])
    plt_tide(pt_tide, pt_time_val, start_date, end_date)
    
    plt.gca().xaxis.tick_top()
    
    #Ferry Plots
    plt.sca(axes[1])
    plt_index = ferry_subsample.xing_num.values==chosen_xing_num

    #Check for existing values in array
    if not np.all( np.isnan( ferry_subsample.Horizontal_speed[plt_index].values)):
        ferry_subsample.Horizontal_speed[plt_index].plot(x='time', y='depth')
    else:
        print('All NaN speed values')
    
    #plot bottom track
    ferry_subsample.bottom_tracking_depth_beam_1[plt_index].plot()

    #format axes
    plt.gca().invert_yaxis()
    plt.ylabel('Depth [m]')

    #format xticks
    xfmt = md.DateFormatter('%m-%d %H:%M')
    axes[1].xaxis.set_major_formatter(xfmt)