import os
import pandas as pd
import matplotlib.pyplot as plt


def load_tide_station_data(station=["NeahBay", "PortTownsend", "PortAngeles"]):
    """
    This function reads the csv files containing the tidal elevation data

    Parameters:
    ---------------
    station - list of strings.   Default = ["NeahBay", "PortTownsend",
                                            "PortAngeles"]
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
               sized=(12, 6)):
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


def interplot(data, start, end):
    """
    This is an interactive function that calls tidal_plot and generates two
    drop down menus with a start time and end time.

    Parameters
    -------------------
    data = a pandas dataframe
        This dataframe should contain tide data

    start = list of strings
        This is a list of all the potential start times

    end = list of strings
        This is a list of all the potential end times

    OUTPUT
    ---------------------
    This function generates a tidal plot from start to end.
    """

    tidal_plot(data, start, end, title="Tide Plot", sized=(12, 6))


def get_list(data):
    """
    This function generates a list of strings from the date time index in data

    Parameters
    -------------------
    data = a pandas dataframe
        This contains a Date Time as index and tidal data

    OUTPUT
    -------------------
    This function returns a list of strings
    """

    out_list = list(data["Date Time"])
    out_list_strings = []
    for i in range(0, len(out_list)):
        out_list_strings.append(str(out_list[i]))
    return out_list_strings


def moon_cycle_exploration(data, cycle_days):
    """
    This function will be used with interact to create a drop down menu
    with the 2014 moon cycle dates.

    Parameters
    ------------------
    data = a pandas dataframe
        This contains the tidal data for 2014

    cycle_days = a list of strings
        This has the days through 2014 that correspond to a given moon phase

    OUTPUT
    --------------------
    This fuction returns a plot of the tide data for the day selected
    """

    day2plot = cycle_days[:4] + "-" + cycle_days[4:6] + "-" + cycle_days[6:8]
    start = day2plot + " 00:00:00"
    end = day2plot + " 23:54:00"
    tidal_plot(data, start, end, title="Tidal Plot", sized=(12, 6))


def multistation_moon(data, cycle_days):
    """
    This function will be used with interact to create a drop down menu
    with the 2014 moon cycle dates and plot the corresponding day for
    the three tidal stations suppled in data.

    Parameters
    -------------------
    data = a list of pandas dataframe objects
        This list will contain the tidal data for the three staitons:
        Neah Bay (NB), Port Townsend (PT), and Port Angeles (PA)
        in that order.

    cycle_days = a list of strings
        This contains the dates in 2014 when a certain moon phase occurs

    OUTPUT
    ---------------------
    This function outputs a matplotlib plot containing three subplots, one
    for each station
    """

    # First we need to parse out the date and set the index to match the
    # format in the dataframe
    day2plot = cycle_days[:4] + "-" + cycle_days[4:6] + "-" + cycle_days[6:8]
    start = day2plot + " 00:00:00"
    end = day2plot + " 23:54:00"

    # Empty list for trimmed datasets
    subset = []
    for station in data:
        temp = trim_data(station, start, end)
        subset.append(temp)

    plt.style.use("ggplot")

    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)

    ax1.plot(subset[0]["Date Time"], subset[0]["Water Level"])
    ax1.set_title("Neah Bay Water Level")

    ax2.plot(subset[1]["Date Time"], subset[1]["Water Level"])
    ax2.set_title("Port Townsend Water Level")

    ax3.plot(subset[2]["Date Time"], subset[2]["Water Level"])
<<<<<<< HEAD
    ax3.set_title("Port Angeles Water Level")
=======
    ax3.set_title("Port Angeles Water Level")


def tidal_plot_all3(data1, data2, data3, start_time, end_time,
                    title="Tidal Elevation", sized=(12, 6)):
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
    This function returns a matplotlib plot with tidal elevations from all
    three ports start_time to end_time with a vertical marker at the specified
    time_index
    """

    subset1 = trim_data(data1, start_time, end_time)
    subset2 = trim_data(data2, start_time, end_time)
    subset3 = trim_data(data3, start_time, end_time)
    f = plt.figure()
    plt.style.use("ggplot")
    plt.subplots(figsize=sized)
    plt.plot(subset1["Date Time"], subset1["Water Level"])
    plt.plot(subset2["Date Time"], subset2["Water Level"])
    plt.plot(subset3["Date Time"], subset3["Water Level"])
    plt.xlabel("Time of Day (GMT)")
    plt.ylabel("Water Height (ft)")
    plt.title(title)
    ax.legend()
    plt.show()
>>>>>>> e9c842703b781d0fbc4599302e17d0fdb0869a6d
