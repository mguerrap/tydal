import numpy as np
import xarray as xr

from ferry_data_utils import ferry_data_QC
from ferry_data_utils import ferry_data_download

URL1 = 'http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/Salish_L1_STA.ncml'
ferry = ferry_data_download(URL1)

ferryQC = ferry_data_QC(ferry,6.5,4,4)

data_May_Jun_2014 = ferryQC.sel(time=slice('2014-05-01T00:00:00', '2014-06-30T00:00:00'))

data_May_Jun_2014.to_netcdf(path='./ferry_data_May_Jun_2014.nc', mode='w')

data_Jul_Aug_2014 = ferryQC.sel(time=slice('2014-07-01T00:00:00', '2014-08-31T00:00:00'))

data_Jul_Aug_2014.to_netcdf(path='./ferry_data_Jul_Aug_2014.nc', mode='w')

data_Sep_Oct_2014 = ferryQC.sel(time=slice('2014-09-01T00:00:00', '2014-10-31T00:00:00'))

data_Sep_Oct_2014.to_netcdf(path='./ferry_data_Sep_Oct_2014.nc', mode='w')

data_Nov_Dec_2014 = ferryQC.sel(time=slice('2014-11-01T00:00:00', '2014-12-31T00:00:00'))

data_Nov_Dec_2014.to_netcdf(path='./ferry_data_Nov_Dec_2014.nc', mode='w')