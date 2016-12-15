import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import Dataset
from matplotlib import path


def ferry_data_download(URL):
    """
    Downloads the ADCP data from ferry
    Inputs:
    URL with the location of the ferry NetCDF file
    Outputs:
    An object containing the link to the ferry data
    """
    ferry = xr.open_dataset(URL)
    return(ferry)


def ferry_data_QC(ferry, TH_abs, TH_u, TH_d):
    """
    Gets the variables and pass a QC to estimate final velocities
    Inputs: ferry data in an xarray DataSet, treshold for absolute
    velocities, TH for true velicities, TH for depth
    Outputs: Quality Controled ferry data in a xarra DataSet
    """
    # QC1: make nan all Absolute velocities that are greater than 6.5 m/s
    absu = ferry.eastward_absolute_water_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    absv = ferry.northward_absolute_water_velocity.where(
        (abs(ferry.eastward_absolute_water_velocity) < TH_abs) &
        (abs(ferry.northward_absolute_water_velocity) < TH_abs))
    absw = ferry.vertical_absolute_water_velocity.where(
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
    u_true = absu + east_btv
    v_true = absv + north_btv
    w_true = absw + vert_btv
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
    """
    adds a variable to ferryQc dataset to mark the crossing number
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

# def count_route_num(ferryQc):
#     """ adds a variable to ferryQc dataset to mark the crossing number

#         INPUTS:
#             ferryQc - the xarray DataSet object with the ferry data
#         OUTPUTS:
#             ferryQc - xarray DataSet object with the ferry data, now with
#                       the added variable, xing_num
#     """
#     #Define on-route box
#     pt1 = (48.134302, -122.758195)
#     pt2 = (48.172176, -122.698912)
#     pt3 = (48.138532, -122.663936)
#     pt4 = (48.101688, -122.727816)
#     p = path.Path([pt1, pt2, pt3, pt4])

#     #check all lat/lon to be on or off route
#     on_route = p.contains_points( list(zip(ferryQc.latitude.values,
#                                            ferryQc.longitude.values)) );

#     #initialize vars
#     counter = 0;
#     xing_num = np.empty((ferryQc.time.size), dtype=int)

#     #Loop through all time values. If off route, give a -9 flag
#     # if on route, give it a route number. If it switches from off route to
#     # on route, increase the route number
#     for ii in range(1, ferryQc.time.size):
#         if not(on_route[ii]):
#             xing_num[ii] = -9
#         else:
#             xing_num[ii] = counter
#         if  (on_route[ii] and not(on_route[ii-1])):
#             counter = counter+1

#     ferryQc['xing_num'] = xr.DataArray(xing_num,
#     								   coords=ferryQc.time.indexes,
#     								   dims=['time'])
#     return(ferryQc)
