import os
import pandas as pd
import matplotlib.pyplot as plt


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


def tidal_plot(data, start_time, end_time, title="Tidal Elevation"):
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


    OUTPUT
    ------------------
    This function returns a matplotlib plot with tidal elevations from
    start_time to end_time with a vertical marker at the specified time_index
    """

    subset = trim_data(data, start_time, end_time)
    f = plt.figure()
    plt.style.use("ggplot")
    plt.xlabel("Time of Day")
    plt.ylabel("Water Height")
    plt.title(title)
    plt.plot(subset["Date Time"], subset["Water Level"])
    plt.show()
