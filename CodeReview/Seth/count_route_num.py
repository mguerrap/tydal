import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import Dataset
from matplotlib import path



def count_route_num(ferryQc):
    """ adds a variable to ferryQc dataset to mark the crossing number

        INPUTS:
            ferryQc - the xarray DataSet object with the ferry data
        OUTPUTS:
            ferryQc - xarray DataSet object with the ferry data, now with
                      the added variable, xing_num
    """
    #Define on-route box 
    pt1 = (48.134302, -122.758195)
    pt2 = (48.172176, -122.698912)
    pt3 = (48.138532, -122.663936)
    pt4 = (48.101688, -122.727816)
    p = path.Path([pt1, pt2, pt3, pt4])

    #check all lat/lon to be on or off route
    on_route = p.contains_points( list(zip(ferryQc.latitude.values, 
                                           ferryQc.longitude.values)) );

    #initialize vars
    counter = 0;
    xing_num = np.empty((ferryQc.time.size), dtype=int)

    #Loop through all time values. If off route, give a -9 flag
    # if on route, give it a route number. If it switches from off route to
    # on route, increase the route number
    for ii in range(1, ferryQc.time.size):
        lat = ferryQc.latitude[ii].values
        lon = ferryQc.longitude[ii].values
        
        if not(on_route[ii]):
            xing_num[ii] = -9
        else:
            xing_num[ii] = counter
        if  (on_route[ii] and not(on_route[ii-1])):
            counter = counter+1
    xing_num = xr.DataArray(xing_num, coords=ferryQc.time.indexes, dims=['time'])
    ferryQc['xing_num'] = xing_num
    
    return(ferryQc)


