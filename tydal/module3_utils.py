import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt


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

    plt.style.use('ggplot')
    plt.subplot(2, 1, 1)
    
    #sub_selected time for vertical bar, as chosen by time_index
    time = pt_tide[start_date:end_date].index[time_index];
    
    plt.plot( pt_tide[start_date:end_date] );
    #eventually get max an min from plot axes?
    max = 10;
    min = -2;
    plt.hold('True')

    #plot vertical line at location specified in time
    plt.plot([time, time], [min, max] )
    
    #Clean up and label axes
    plt.ylabel('Elevation [m]')
    plt.gcf().autofmt_xdate()
