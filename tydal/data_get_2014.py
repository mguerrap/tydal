import requests
import os
import pandas as pd

# Dictionary of station names to ID numbers
station_names_to_id = {"NeahBay": "9443090", "PortAngeles": "9444090",
                       "PortTownsend": "9444900"}

# Dictionary of station ID numbers to names
station_id_to_names = {"9443090": "NeahBay", "9444090": "PortAngeles",
                       "9444900": "PortTownsend"}

# List of month start dates
start_list = ["20140101", "20140201", "20140301", "20140401", "20140501",
              "20140601", "20140701", "20140801", "20140901", "20141001",
              "20141101", "20141201"]

# List of month end dates
end_list = ["20140131", "20140228", "20140331", "20140430", "20140531",
            "20140630", "20140731", "20140831", "20140930", "20141031",
            "20141130", "20141231"]

# Create empty DataFrame to hold the data
data = pd.DataFrame()
# Create empty list to hold the file names
filenames = []


def get_data_2014(station="9444900", begin="20140101", end="20140131"):
    """
    This fuction gets the data from 2014 in month chunks.
    The NOAA site limits data requests to one month.

    Parameters
    ------------
    station : string, default = "9444900" Port Townsend station
        The tide station ID that the data is coming from

    begin : string, default = "20140101", January 1st, 2014
        The start date of the data set

    end : string, default = "20140131", January 31st, 2014
    The end date of the data set
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
    filenames.append(outfile)


# Collects the data for the whole year saved in monthly csv files
for station in station_names_to_id:
    # Gets the data for each station
    for i in range(0, len(start_list)):
        get_data_2014(station_names_to_id[station], start_list[i], end_list[i])
    # For each station set of data, read the files and convert to one file
    for i in range(0, len(filenames)):
        buff = pd.read_csv(filenames[i])
        data = data.append(buff)
    # Sets outfile to the station name and year
    outfile = ("2014_" + station_id_to_names[filenames[0][0:7]] + ".csv")
    data.to_csv(outfile)
    # Want to remove monthly files
    first = os.getcwd()
    for i in range(0, len(filenames)):
        os.remove(first + "/" + filenames[i])
    # Resets filenames and data
    filenames = []
    data = pd.DataFrame()
