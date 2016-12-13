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
start_list = ["0101", "0201", "0301", "0401", "0501", "0601", "0701", "0801",
              "0901", "1001", "1101", "1201"]

# List of month end dates
end_list = ["0131", "0228", "0331", "0430", "0531", "0630", "0731", "0831",
            "0930", "1031", "1130", "1231"]

# Create empty DataFrame to hold the data
data = pd.DataFrame()
# Create empty list to hold the file names
filenames = []


def get_data_year(station="9444900", begin="0101", end="0131", year="2014"):
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
    # Concatinate the year to the start and end dates
    first_index = year + begin
    second_index = year + end
    URL = ("https://tidesandcurrents.noaa.gov/api/datagetter?product=water_" +
           "level&application=NOS.COOPS.TAC.WL&station=" + station + "&" +
           "begin_date=" + first_index + "&end_date=" + second_index +
           "&datum=MLLW&units=" + "english&time_zone=GMT&format=csv")
    outfile = station + first_index + ".csv"
    req = requests.get(URL)
    assert req.status_code == 200
    with open(outfile, "wb") as f:
        f.write(req.content)
    filenames.append(outfile)


# Prompts the user for the year of data they want
year = str(input("What year of data do you want? "))
# Collects the data for the whole year saved in monthly csv files
for station in station_names_to_id:
    # Gets the data for each station
    for i in range(0, len(start_list)):
        get_data_year(station_names_to_id[station], start_list[i],
                      end_list[i], year)
    # For each station set of data, read the files and convert to one file
    for i in range(0, len(filenames)):
        buff = pd.read_csv(filenames[i])
        # Drop the unnecessary columns from the data
        buff.drop(buff.columns[[3, 4, 5, 6, 7]], axis=1, inplace=True)
        # Trim off the white space on the column names
        buff.columns = ["Date Time", "Water Level", "Sigma"]
        data = data.append(buff)
    # Sets outfile to the station name and year
    outfile = (year + "_" + station_id_to_names[filenames[0][0:7]] + ".csv")
    data.to_csv(outfile)
    # Want to remove monthly files
    first = os.getcwd()
    for i in range(0, len(filenames)):
        os.remove(first + "/" + filenames[i])
    # Resets filenames and data
    filenames = []
    data = pd.DataFrame()
