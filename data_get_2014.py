import requests
import os
import pandas as pd

# List of the station ID numbers
station_id = {"Neah Bay": "9443090", "Port Angeles": "9444090",
	"Port Townsend": "9444900"}

# List of month start dates
start_list = ["20140101", "20140201", "20140301", "20140401", "20140501",
	"20140601", "20140701", "20140801", "20140901", "20141001", "20141101"
	"20141201"]

# List of month end dates
end_list = ["20140131", "20140228", "20140331", "20140430", "20140531",
	"20140630", "20140731", "20140831", "20140930", "20141031", "20141130"
	"20141231"]

# Create empty DataFrame to hold the data



def get_data_2014 (station, begin, end):
	"""
	This fuction gets the data from 2014 in month chunks.
	The NOAA site limits data requests to one month.
	"""
	URL = ("https://tidesandcurrents.noaa.gov/api/datagetter?product=water_" +
		"level&application=NOS.COOPS.TAC.WL&station=" + station + "&" +
		"begin_date=" + begin + "&end_date=" + end + "&datum=MLLW&units=" +
		"english&time_zone=GMT&format=csv")
	outfile = station + begin + ".csv"
	req = requests.get(URL)
	assert req.status_code == 200
	with open(outfile, "wb") as f:
		f.write(req.content)

# Collects the data for the whole year saved in monthly csv files
for station in station_id:
	for i in range(0, len(start_list)-1):
		get_data_2014(station_id[station], start_list[i], end_list[i])
