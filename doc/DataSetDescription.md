# Data Sets
We will use two data sets for our project:

## 1. Tidal Elevation data from NOOA tidal gauges in the Strait of San Juan de Fuca:
We will use data from the following stations:
* Neah Bay (ID 9443090)
* Port Angeles (ID 9444090)
* Port Townsend (ID 9444900)

Tidal elevation data for each station is available in .csv format on the NOAA website https://tidesandcurrents.noaa.gov/stations.html

The site allows to download a month of tidal elevation data at a time. The .csv files contain two columns: time and water elevation. There is data every 6 minutes (240 data points per day per station). We will use a maximum of 12 months of data.

## 2. Tidal currents from Acoustic Doppler Current Profilers (ADCPs) from the Ferry-Based Monitoring of Puget Sound Currents project 

Information about this project is available in:

http://www.apl.washington.edu/project/project.php?id=ferries_for_science

There are ADCPs installed on board two WDOT ferries, the Kennewik and the Salish, which run the Port Townsend - Coupeville route about 12 times a day depending on the season. ADCPs measure current velocities through the water column while the ferry is runing. The ADCPs record vertical profiles of water velocity, taking measurements every second at 60 points through the water column (every 2 meters up to 120 meters from the sea surface down to the sea bottom).

Data is available on two websites (on for each ferry ADCP)
http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/Salish_L1_STA.ncml.html
http://107.170.217.21:8080/thredds/dodsC/Kennewick_L1_STA/Kennewick_L1_STA.ncml.html

Data can be downloaded as a netCDF file. We will use the following variables from the data set, which will allow us to perform quality control of the data and estimate the tidal currents velocities.

* Depth
* Time
* Latitude
* Longitude
* Bottom tracking depths (1 to 4)
* East, North and Vertical absolute water velocity
* East, North and Vertical bottom tracking velocity
* Echo amplitudes (1 to 4)
* Beam Correlations (1 to 4)
* Tide prediction
* DEM bathymetry

There is one netCDF file for each ferry and we can download the entire data set up to date (the dataset grows every day while the ferries are running). Data has been recorded since May 2014, and there are 983774 vertical profiles available from the Salish ADCP and 1007317 vertical profiles available from the Kennewick.


