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


def get_data_year(station="9444900", begin="0101", end="0131", year="2014"):
    """
    This fuction gets the data from a year in month chunks.
    The NOAA site limits data requests to one month.

    The defaults are set for this function to get the 2014 data from the
    Port Townsend tide station.

    Parameters
    ------------
    station : string, default = "9444900" Port Townsend station
        The tide station ID that the data is coming from

    begin : string, default = "0101", January 1st
        The start date of the data set

    end : string, default = "0131", January 31st
        The end date of the data set

    year : string, default = "2014", 2014
        The year of data to be accessed
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


def month_files_to_year(file_list):
    '''
    This function takes the monthly tide data files generated from the
    data_get_year() function and concatenates them into a single file
    for each station.

    Parameters
    ------------------
    file_list : list of strings
        This list contains the names of the monthly files generated from
        the get_data_year() function
    '''
    # Create empty dataframe object to hold the data
    data = pd.DataFrame()
    # read the files and convert to one file
    for i in range(0, len(file_list)):
        buff = pd.read_csv(file_list[i])
        # Drop the unnecessary columns from the data
        buff.drop(buff.columns[[3, 4, 5, 6, 7]], axis=1, inplace=True)
        # Trim off the white space on the column names
        buff.columns = ["Date Time", "Water Level", "Sigma"]
        # Append to the data DataFrame
        data = data.append(buff)
    # Sets outfile to the station name and year
    outfile = (year + "_" + station_id_to_names[file_list[0][0:7]] + ".csv")
    # Set the index to the Date Time
    data = data.set_index(data["Date Time"])
    # Writes data to the outfile
    data.to_csv(outfile)


def remove_month_files(file_list):
    '''
    This function removes the month files generated during the data download.

    Parameters
    --------------------
    file_list : list of strings
        This list contains the names of the monthly files generated from
        the get_data_year() function
    '''
    # First, we get the current working directory
    first = os.getcwd()
    # Cycle through the list of file names and remove them
    for i in range(0, len(file_list)):
        os.remove(first + "/" + file_list[i])


# Create empty list to hold the file names
filenames = []
# Prompts the user for the year of data they want
year = str(input("What year of data do you want? (from 1996 to 2016): "))
if year < "1996" or year > "2016":
    raise Exception("Not a valid year. Please try again.")
# Main code body that collects the data for the whole year saves it
# in monthly csv files
# Runs the same code for each station in dictionary above
for station in station_names_to_id:
    # Gets the data for each station
    for i in range(0, len(start_list)):
        get_data_year(station_names_to_id[station], start_list[i],
                      end_list[i], year)
    # For each station set of data, read the files and convert to one file
    month_files_to_year(filenames)
    # For each station set of data, remove the monthly files, so only the
    # year file remains
    remove_month_files(filenames)
    # reset the file names list and dataframe to empty
    filenames = []
