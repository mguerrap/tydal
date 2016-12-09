import os
import pandas as pd
import matplotlib.pyplot as plt


def load_tide_station_data(station=["NeahBay", "PortTownsend", "PortAngeles"]):
    """
    This function reads the csv files containing the tidal elevation data

    Parameters:
    ---------------
    station - list of strings.   Default = ["NeahBay", "PortTownsend", "PortAngeles"]
        A list containing the station name(s). 

    Output:
    ----------------
    This function returns a list containing dataframe objects
    """
    
    # Empty list and dataframe for data assembly
    data_list = []
    data = pd.DataFrame()
    # List of years that we have already downloaded data for
    years = ["2014", "2015", "2016"]
    # Iterate through station list
    for stat in station:
        # Iterate through year list
        for year in years:
            # Assemble filename
            filename = "./Data/" + year + "_" + stat + ".csv"
            # Read in first file
            temp = pd.read_csv(filename, parse_dates=["Date Time"])
            # append to data repeat for next years
            data = data.append(temp)
        # Remove excess column in data
        data.drop(data.columns[[0]], axis=1, inplace=True)
        # Append station data to data_list
        data_list.append(data)
        # Reset data for next station
        data = pd.DataFrame()
    return data_list


def trim_data(data, start, end):
    """
    This function takes in a dataframe object and trims it to the two supplied
    time indexes.

    Parameters:
    ---------------------
    data - pandas DataFrame object
        A dataframe containing the tidal elevation data

    start - string
        A string of the format "yyyy-mm-dd hh:mm:ss" denoting the start index

    end - string
        A string of the format "yyyy-mm-dd hh:mm:ss" denoting the end index

    OUTPUT:
    --------------
    This function returns a dataframe object that has been trimmed to start
    and end indexes given
    """

    data = data.set_index(data["Date Time"])
    subset = data.loc[start:end]
    return subset


def tidal_plot(data, start_time, end_time, title="Tidal Elevation",
               sized=(12,6)):
    """
    This function takes in a dataframe object, a start and end time, and a time
    index.  It generates a plot from start to end of tidal elevation from data.
    There is a vertical marker at the location specified in time_index.

    Parameters:
    ------------------
    data - pandas DataFrame object
        A dataframe containing the tidal elevation data

    start_time - string
        A string of the format "yyyy-mm-dd hh:mm:ss" in six minute intervals
        on the minute  (e.g. "2014-03-15 12:36:00")

    end_time - string
        A string of the format "yyyy-mm-dd hh:mm:ss" in six minute intervals
        on the minute (e.g. "2014-03-16 12:48:00")

    title - string
        A string to be the title of the generated plot

    sized - touple
        A touple to be the size of the generated figure (width, height)


    OUTPUT
    ------------------
    This function returns a matplotlib plot with tidal elevations from
    start_time to end_time with a vertical marker at the specified time_index
    """

    subset = trim_data(data, start_time, end_time)
    f = plt.figure()
    plt.style.use("ggplot")
    plt.subplots(figsize=sized)
    plt.xlabel("Time of Day (GMT)")
    plt.ylabel("Water Height (ft)")
    plt.title(title)
    plt.plot(subset["Date Time"], subset["Water Level"])
    plt.show()
