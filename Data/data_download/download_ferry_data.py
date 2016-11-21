import numpy as numpy
import pandas as pd
from netCDF4 import Dataset


def download_ferry_data(URL):
	"""Downloads the ADCP data from ferry"""
	#Inputs:
	# URL with the location of the ferry NetCDF file
	#Outputs:
	# An object containing the link to the ferry data
	ferry=Dataset(URL, 'r')

	return(ferry)

def ferry_data(ferry):
	"""Gets the variables that will be used in the data analysis"""
	#Inputs:
	#Ferry object
	#Outputs:
	#A dataframe containing the current data from ferries for QC process

	# Load info about variables
	lat = ferry.variables['latitude']
	lon = ferry.variables['longitude']
	time = ferry.variables['time']
	ensemble = ferry.varibales['ensemble']
	dem = ferry.variables['psdem_bathymetry_navd88']
	depth = ferry.variables['depth']
	pstide = ferry.variables['pstide_prediction_mllw']
	bt_1 = ferry.variables['bottom_tracking_depth_beam_1']
	bt_2 = ferry.variables['bottom_tracking_depth_beam_2']
	bt_3 = ferry.variables['bottom_tracking_depth_beam_3']
	bt_4 = ferry.variables['bottom_tracking_depth_beam_4']

	speedmg = ferry.variables['speed_made_good']
	absu =  ferry.variables['eastward_absolute_water_velocity']
	absv =  ferry.variables['northward_absolute_water_velocity']
	absw =  ferry.variables['vertical_absolute_water_velocity']

	east_btv = ferry.variables['eastward_bottom_tracking_velocity']
	north_btv = ferry.variables['northward_bottom_tracking_velocity']
	vert_btv = ferry.variables['vertical_bottom_tracking_velocity']

	e_absU = ferry.variables['error_absolute_water_velocity']
	e_btU = ferry.variables['error_bottom_tracking_velocity']

	corr1 = ferry.variables['correlation_beam1']
	corr2 = ferry.variables['correlation_beam2']
	corr3 = ferry.variables['correlation_beam3']
	corr4 = ferry.variables['correlation_beam4']

	pg1 = ferry.variables['percent_good_field_1']
	pg2 = ferry.variables['percent_good_field_2']
	pg3 = ferry.variables['percent_good_field_3']
	pg4 = ferry.variables['percent_good_field_4']

	# Load single dimension data into a dataframe
	df = pd.DataFrame()
	df['latitude'] = lat[:]
	df['longitude'] = lon[:]



