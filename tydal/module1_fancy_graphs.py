#module1_fancy_graphs create graphs with moon and text for module 1
#Written by: Amie Adams
#Import relevant packages
import os
import numpy as np
import pandas as pd
from datetime import date
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as IM
import matplotlib._png
from matplotlib._png import read_png

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

def plot_NB_Full_to_Full():
	    """
    This function takes generates a plot during from one full moon to the next at NeahBay.
    There is a marker in text and .png form to visualize the phases of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phases of the moon
    """
	#load specific data
	subset = module1_utils.trim_data(NB, "2014-11-01 00:00:00", "2014-12-10 00:00:00")

	fig, ax = plt.subplots(figsize=(15, 8))

	# Add Text for first Full moon
	offsetboxFull1 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull1 = [Full_2014_dates[10], 14.5]
	abTextFull1 = AnnotationBbox(offsetboxFull1, xyTextFull1,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull1)

	# add Full moon image to first full moon spot
	FullMoon = plt.imread("./Figures/FullMoonA.png")
	imageboxFull = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull = [Full_2014_dates[10], 13]               # coordinates to position this image
	abMoonFull = AnnotationBbox(imageboxFull, xyMoonFull,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull)

	# Add Text Third
	offsetboxThird = TextArea("Third Quarter", minimumdescent=False)
	xyTextThird = [Third_2014_dates[10], 14.5]
	abTextThird = AnnotationBbox(offsetboxThird, xyTextThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextThird)

	# add Third moon image
	ThirdMoon = plt.imread("./Figures/ThreeQuarterMoonA.png")
	imageboxThird= OffsetImage(ThirdMoon, zoom=.5)
	xyMoonThird = [Third_2014_dates[10], 13]               # coordinates to position this image
	abMoonThird = AnnotationBbox(imageboxThird, xyMoonThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonThird)

	# Add Text First
	offsetboxFirst = TextArea("First Quarter", minimumdescent=False)
	xyTextFirst = [First_2014_dates[11], 14.5]
	abTextFirst = AnnotationBbox(offsetboxFirst, xyTextFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFirst)

	# add First moon image
	FirstMoon = plt.imread("./Figures/FirstQuarterA.png")
	imageboxFirst = OffsetImage(FirstMoon, zoom=.5)
	xyMoonFirst = [First_2014_dates[11], 13]               # coordinates to position this image
	abMoonFirst = AnnotationBbox(imageboxFirst, xyMoonFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFirst)

	# Add Text New
	offsetbox = TextArea("New Moon", minimumdescent=False)
	xyTextNew = [New_2014_dates[11], 14.5]
	abTextNew = AnnotationBbox(offsetbox, xyTextNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew)

	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew = [New_2014_dates[11], 13]               # coordinates to position this image
	abMoonNew = AnnotationBbox(imageboxNew, xyMoonNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew)

	# Add Text Full moon 2
	offsetboxFull2 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull2 = [Full_2014_dates[11], 14.5]
	abTextFull2 = AnnotationBbox(offsetboxFull2, xyTextFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull2)

	# add Full moon 2 image 
	imageboxFull2 = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull2 = [Full_2014_dates[11], 13]               # coordinates to position this image
	abMoonFull2 = AnnotationBbox(imageboxFull2, xyMoonFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull2)

	plt.title('Effects of position of the Moon relative to the Earth and Sun on the strength of the tides at Neah Bay')
	plt.style.use('ggplot')
	#Expand graph height
	plt.plot(Third_2014_dates[10],14.5)
	#Plot tide data
	plt.plot(subset["Date Time"], subset["Water Level"])
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	plt.draw()
	plt.show()

def plot_PT_Full_to_Full():
	    """
    This function takes generates a plot during from one full moon to the next at Port Townsend.
    There is a marker in text and .png form to visualize the phases of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phases of the moon
    """
	#load specific data
	subset = module1_utils.trim_data(PT, "2014-11-01 00:00:00", "2014-12-10 00:00:00")

	fig, ax = plt.subplots(figsize=(15, 8))

	# Add Text for first Full moon
	offsetboxFull1 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull1 = [Full_2014_dates[10], 14.5]
	abTextFull1 = AnnotationBbox(offsetboxFull1, xyTextFull1,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull1)

	# add Full moon image to first full moon spot
	FullMoon = plt.imread("./Figures/FullMoonA.png")
	imageboxFull = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull = [Full_2014_dates[11], 13]               # coordinates to position this image
	abMoonFull = AnnotationBbox(imageboxFull, xyMoonFull,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull)

	# Add Text Third
	offsetboxThird = TextArea("Third Quarter", minimumdescent=False)
	xyTextThird = [Third_2014_dates[10], 14.5]
	abTextThird = AnnotationBbox(offsetboxThird, xyTextThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextThird)

	# add Third moon image
	ThirdMoon = plt.imread("./Figures/ThreeQuarterMoonA.png")
	imageboxThird= OffsetImage(ThirdMoon, zoom=.5)
	xyMoonThird = [Third_2014_dates[10], 13]               # coordinates to position this image
	abMoonThird = AnnotationBbox(imageboxThird, xyMoonThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonThird)

	# Add Text First
	offsetboxFirst = TextArea("First Quarter", minimumdescent=False)
	xyTextFirst = [First_2014_dates[11], 14.5]
	abTextFirst = AnnotationBbox(offsetboxFirst, xyTextFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFirst)

	# add First moon image
	FirstMoon = plt.imread("./Figures/FirstQuarterA.png")
	imageboxFirst = OffsetImage(FirstMoon, zoom=.5)
	xyMoonFirst = [First_2014_dates[11], 13]               # coordinates to position this image
	abMoonFirst = AnnotationBbox(imageboxFirst, xyMoonFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFirst)

	# Add Text New
	offsetbox = TextArea("New Moon", minimumdescent=False)
	xyTextNew = [New_2014_dates[11], 14.5]
	abTextNew = AnnotationBbox(offsetbox, xyTextNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew)

	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew = [New_2014_dates[11], 13]               # coordinates to position this image
	abMoonNew = AnnotationBbox(imageboxNew, xyMoonNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew)

	# Add Text Full moon 2
	offsetboxFull2 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull2 = [Full_2014_dates[11], 14.5]
	abTextFull2 = AnnotationBbox(offsetboxFull2, xyTextFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull2)

	# add Full moon 2 image 
	imageboxFull2 = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull2 = [Full_2014_dates[11], 13]               # coordinates to position this image
	abMoonFull2 = AnnotationBbox(imageboxFull2, xyMoonFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull2)

	plt.title('Effects of position of the Moon relative to the Earth and Sun on the strength of the tides at Port Townsend')
	plt.style.use('ggplot')
	#Expand graph height
	plt.plot(Third_2014_dates[10],14.5)
	#Plot tide data
	plt.plot(subset["Date Time"], subset["Water Level"])
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	plt.draw()
	plt.show()

def plot_PA_Full_to_Full():
	"""
    This function takes generates a plot during from one full moon to the next at Port Angeles.
    There is a marker in text and .png form to visualize the phases of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phases of the moon
    """
	#load specific data
	subset = module1_utils.trim_data(PA, "2014-11-01 00:00:00", "2014-12-10 00:00:00")
	
	fig, ax = plt.subplots(figsize=(15, 8))

	# Add Text for first Full moon
	offsetboxFull1 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull1 = [Full_2014_dates[10], 14.5]
	abTextFull1 = AnnotationBbox(offsetboxFull1, xyTextFull1,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull1)

	# add Full moon image to first full moon spot
	FullMoon = plt.imread("./Figures/FullMoonA.png")
	imageboxFull = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull = [Full_2014_dates[11], 13]               # coordinates to position this image
	abMoonFull = AnnotationBbox(imageboxFull, xyMoonFull,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull)

	# Add Text Third
	offsetboxThird = TextArea("Third Quarter", minimumdescent=False)
	xyTextThird = [Third_2014_dates[10], 14.5]
	abTextThird = AnnotationBbox(offsetboxThird, xyTextThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextThird)

	# add Third moon image
	ThirdMoon = plt.imread("./Figures/ThreeQuarterMoonA.png")
	imageboxThird= OffsetImage(ThirdMoon, zoom=.5)
	xyMoonThird = [Third_2014_dates[10], 13]               # coordinates to position this image
	abMoonThird = AnnotationBbox(imageboxThird, xyMoonThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonThird)

	# Add Text First
	offsetboxFirst = TextArea("First Quarter", minimumdescent=False)
	xyTextFirst = [First_2014_dates[11], 14.5]
	abTextFirst = AnnotationBbox(offsetboxFirst, xyTextFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFirst)

	# add First moon image
	FirstMoon = plt.imread("./Figures/FirstQuarterA.png")
	imageboxFirst = OffsetImage(FirstMoon, zoom=.5)
	xyMoonFirst = [First_2014_dates[11], 13]               # coordinates to position this image
	abMoonFirst = AnnotationBbox(imageboxFirst, xyMoonFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFirst)

	# Add Text New
	offsetbox = TextArea("New Moon", minimumdescent=False)
	xyTextNew = [New_2014_dates[11], 14.5]
	abTextNew = AnnotationBbox(offsetbox, xyTextNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew)

	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew = [New_2014_dates[11], 13]               # coordinates to position this image
	abMoonNew = AnnotationBbox(imageboxNew, xyMoonNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew)

	# Add Text Full moon 2
	offsetboxFull2 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull2 = [Full_2014_dates[11], 14.5]
	abTextFull2 = AnnotationBbox(offsetboxFull2, xyTextFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull2)

	# add Full moon 2 image 
	imageboxFull2 = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull2 = [Full_2014_dates[11], 13]               # coordinates to position this image
	abMoonFull2 = AnnotationBbox(imageboxFull2, xyMoonFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull2)

	plt.title('Effects of position of the Moon relative to the Earth and Sun on the strength of the tides at Port Angeles')
	plt.style.use('ggplot')
	#Expand graph height
	plt.plot(Third_2014_dates[10],14.5)
	#Plot tide data
	plt.plot(subset["Date Time"], subset["Water Level"])
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	plt.draw()
	plt.show()

def plot_3Station_FullMoon():
	"""
    This function takes generates a plot during from one full moon with a buffer on each side at each port.
    There is a marker in text and .png form to visualize the phase of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phase of the moon
    """
	#load specific data
	NB08082014 = trim_data(NB, "2014-08-08 00:00:00", "2014-08-12 00:00:00")
	PT08082014 = trim_data(PT, "2014-08-08 00:00:00", "2014-08-12 00:00:00")
	PA08082014 = trim_data(PA, "2014-08-08 00:00:00", "2014-08-12 00:00:00")

	fig, ax = plt.subplots(figsize=(20, 10))
	
	# Add Text Full
	offsetboxFull = TextArea("Full Moon", minimumdescent=False)
	xyTextFull = [Full_2014_dates[7], 11]
	abTextFull = AnnotationBbox(offsetboxFull, xyTextFull,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull)
	
	# add Full moon image
	FullMoon = plt.imread("./Figures/FullMoonA.png")
	imageboxFull = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull = [Full_2014_dates[7], 10]               # coordinates to position this image
	abMoonFull = AnnotationBbox(imageboxFull, xyMoonFull,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull)

	#Expand graph height
	plt.plot(New_2014_dates[9],11)
	plt.title('New Moon in August 2014 and Tides of the 3 Ports')
	plt.style.use('ggplot')
	plt.plot(NB08082014["Date Time"], NB08082014["Water Level"], label = 'Neah Bay')
	plt.plot(PT08082014["Date Time"], PT08082014["Water Level"], label = 'Port Townsend')
	plt.plot(PA08082014["Date Time"], PA08082014["Water Level"], label = 'Port Angeles')
	
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	ax.legend()
	plt.draw()
	plt.show()

def plot_3Station_NewMoon():
	"""
    This function takes generates a plot during from one New moon with a buffer on each side at each port.
    There is a marker in text and .png form to visualize the phase of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phase of the moon
    """
	#load specific data
	NB09212014 = trim_data(NB, "2014-09-21 00:00:00", "2014-09-24 00:00:00")
	PT09212014 = trim_data(PT, "2014-09-21 00:00:00", "2014-09-24 00:00:00")
	PA09212014 = trim_data(PA, "2014-09-21 00:00:00", "2014-09-24 00:00:00")

	fig, ax = plt.subplots(figsize=(20, 10))
	
	# Add Text New
	offsetboxNew = TextArea("New Moon", minimumdescent=False)
	xyTextNew = [New_2014_dates[9], 11]
	abTextNew = AnnotationBbox(offsetboxNew, xyTextNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew)
	
	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew = [New_2014_dates[9], 10]               # coordinates to position this image
	abMoonNew = AnnotationBbox(imageboxNew, xyMoonNew,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew)
	
	#Expand graph height
	plt.plot(New_2014_dates[9],11)
	plt.title('New Moon in September 2014 and Tides of the 3 Ports')
	plt.style.use('ggplot')
	plt.plot(NB09212014["Date Time"], NB09212014["Water Level"], label = 'Neah Bay')
	plt.plot(PT09212014["Date Time"], PT09212014["Water Level"], label = 'Port Townsend')
	plt.plot(PA09212014["Date Time"], PA09212014["Water Level"], label = 'Port Angeles')
	
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	ax.legend()
	plt.draw()
	plt.show()

def plot_3Station_ThirdMoon():
	"""
    This function takes generates a plot during from one Third Quarter moon with a buffer on each side at each port.
    There is a marker in text and .png form to visualize the phase of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phase of the moon
    """
	#load specific data
	NB07162014 = trim_data(NB, "2014-07-16 00:00:00", "2014-07-20 00:00:00")
	PT07162014 = trim_data(PT, "2014-07-16 00:00:00", "2014-07-20 00:00:00")
	PA07162014 = trim_data(PA, "2014-07-16 00:00:00", "2014-07-20 00:00:00")

	fig, ax = plt.subplots(figsize=(20, 10))
	
	# Add Text Third
	offsetboxThird = TextArea("Third Moon", minimumdescent=False)
	xyTextThird = [Third_2014_dates[6], 11.75]
	abTextThird = AnnotationBbox(offsetboxThird, xyTextThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextThird)
	
	# add Third moon image
	ThirdMoon = plt.imread("./Figures/ThreeQuarterMoonA.png")
	imageboxThird= OffsetImage(ThirdMoon, zoom=.5)
	xyMoonThird = [Third_2014_dates[6], 10.75]               # coordinates to position this image
	abMoonThird = AnnotationBbox(imageboxThird, xyMoonThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonThird)
	
	#Expand graph height
	plt.plot(Third_2014_dates[6],12)
	plt.title('Third Quarter Moon in July 2014 and Tides of the 3 Ports')
	plt.style.use('ggplot')
	plt.plot(NB07162014["Date Time"], NB07162014["Water Level"], label = 'Neah Bay')
	plt.plot(PT07162014["Date Time"], PT07162014["Water Level"], label = 'Port Townsend')
	plt.plot(PA07162014["Date Time"], PA07162014["Water Level"], label = 'Port Angeles')
	
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	ax.legend()
	plt.draw()
	plt.show()

def plot_3Station_FirstMoon():
	"""
    This function takes generates a plot during from one First quarter moon with a buffer on each side at each port.
    There is a marker in text and .png form to visualize the phase of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phase of the moon
    """
	#load specific data
	NB05042014 = trim_data(NB, "2014-05-04 00:00:00", "2014-05-08 00:00:00")
	PT05042014 = trim_data(PT, "2014-05-04 00:00:00", "2014-05-08 00:00:00")
	PA05042014 = trim_data(PA, "2014-05-04 00:00:00", "2014-05-08 00:00:00")

	fig, ax = plt.subplots(figsize=(20, 10))
	
	# Add Text First
	offsetboxFirst = TextArea("First Moon", minimumdescent=False)
	xyTextFirst = [First_2014_dates[4], 11]
	abTextFirst = AnnotationBbox(offsetboxFirst, xyTextFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFirst)

	# add First moon image
	FirstMoon = plt.imread("./Figures/FirstQuarterA.png")
	imageboxFirst = OffsetImage(FirstMoon, zoom=.5)
	xyMoonFirst = [First_2014_dates[4], 10]               # coordinates to position this image
	abMoonFirst = AnnotationBbox(imageboxFirst, xyMoonFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFirst)
	
	#Expand graph height
	plt.plot(First_2014_dates[4],11)
	plt.title('First Quarter Moon in May 2014 and Tides of the 3 Ports')
	plt.style.use('ggplot')
	plt.plot(NB05042014["Date Time"], NB05042014["Water Level"], label = 'Neah Bay')
	plt.plot(PT05042014["Date Time"], PT05042014["Water Level"], label = 'Port Townsend')
	plt.plot(PA05042014["Date Time"], PA05042014["Water Level"], label = 'Port Angeles')
	
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	ax.legend()
	plt.draw()
	plt.show()

def find_local_min(NB06012014):
 	"""
 	This function takes in a dataframe object and looking for a local minimum 
 	and setting arrays for values to be entered into

    Parameters:
    ---------------------
    NB06012014 - pandas DataFrame object
        A dataframe containing the tidal elevation data of one day
	Output-an array
	local mins 
	"""
	min_x = []
	min_y = []
	local_min = []

	for i in range(1, NB06012014.size):
	    if (i==0):
	    #do nothing-skip header
	    elif((NB06012014[1,i]-NB06012014[1,i+1])<NB06012014[1,i]-NB06012014[1,i+1]):
		    if((NB06012014[1,i+1]-NB06012014[1,i+2])>(NB06012014[1,i+1]-NB06012014[1,i+2])):
		       min_x = [min_x, NB06012014[0,i]]
		       min_y = [min_y, NB06012014[1,i]]
		   else():
		   	#do nothing
	    else():
	    #do nothing

	local_min = min_x.append(min_y)
	return local_min

def find_local_max(NB06012014):
 	"""
 	This function takes in a dataframe object and looking for a local max 
 	and setting arrays for values to be entered into

    Parameters:
    ---------------------
    NB06012014 - pandas DataFrame object
        A dataframe containing the tidal elevation data of one day
	Output-an array
	local maxs
	"""
	max_x = []
	max_y = []
	local_max = []

	for i in range(1, NB06012014.size):
	    if (i==0):
	    #do nothing-skip header
	    elif((NB06012014[1, i] - NB06012014[1, i + 1]) > (NB06012014[1, i] - NB06012014[1, i + 1])):
	    	if ((NB06012014[1, i + 1] - NB06012014[1, i + 2]) < (NB06012014[1, i + 1] - NB06012014[1, i + 2])):
		       max_x = [max_x, NB06012014[0, i]]
		       max_y = [max_y, NB06012014[1, i]]
		    else():
		   	#do nothing
	    else():
	    #do nothing

	local_max = max_x.append(max_y)
	return local_max

def plot_3Station_High_Low():
	"""
 	This function plot local min and maxs for three ports 
 	and setting arrays for values to be entered into

	Output-Plot
	"""
	NB06012014 = trim_data(NB, "2014-06-01 00:00:00", "2014-06-02 00:00:00")
	PT06012014 = trim_data(PT, "2014-06-01 00:00:00", "2014-06-02 00:00:00")
	PA06012014 = trim_data(PA, "2014-06-01 00:00:00", "2014-06-02 00:00:00")
	#Looking for a local minimum and maxima and setting arrays for values to be entered into
	NB_min = find_local_min(NB06012014)
	NB_max = find_local_max(NB06012014)
	PT_min = find_local_min(PT06012014)
	PT_max = find_local_max(PT06012014)
	PA_min = find_local_min(PA06012014)
	PA_max = find_local_max(PA06012014)
	#Plot one day of data
	plt.style.use('ggplot')
	fig, ax = plt.subplots(figsize=(12, 6))
	plt.plot(data01012014['Time'], data01012014['Water Level'])
	plt.scatter(NB_min_x, -2, 'g')
	plt.scatter(NB_max_x, 10, 'r')
	plt.scatter(PT_min_x, -2, 'g')
	plt.scatter(PT_max_x, 10, 'r')
	plt.scatter(PA_min_x, -2, 'g')
	plt.scatter(PA_max_x, 10, 'r')
	plt.xlabel("Time (Hours)")
	plt.ylabel("Water Depth based on MLLW")
	ax.set_title("Water Level by Time showing High and Low Tide")
	plt.show()
	



def plot_NB_New_to_New():
	    """
    This function takes generates a plot during from one New moon to the next at NeahBay.
    There is a marker in text and .png form to visualize the phases of the moon and the tides at once

    Parameters:
    ------------------
    
    OUTPUT
    ------------------
    This function returns a matplotlib plot with markers for the phases of the moon
    """
	#load specific data
	subset = module1_utils.trim_data(NB, "2014-05-23 00:00:00", "2014-06-30 00:00:00")

	fig, ax = plt.subplots(figsize=(15, 8))

	# Add Text New1
	offsetbox1 = TextArea("New Moon", minimumdescent=False)
	xyTextNew1 = [New_2014_dates[5], 14.5]
	abTextNew1 = AnnotationBbox(offsetbox1, xyTextNew1,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew1)

	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew1 = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew1 = [New_2014_dates[5], 13]               # coordinates to position this image
	abMoonNew1 = AnnotationBbox(imageboxNew1, xyMoonNew1,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew1)
	
	# Add Text First
	offsetboxFirst = TextArea("First Quarter", minimumdescent=False)
	xyTextFirst = [First_2014_dates[5], 14.5]
	abTextFirst = AnnotationBbox(offsetboxFirst, xyTextFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFirst)

	# add First moon image
	FirstMoon = plt.imread("./Figures/FirstQuarterA.png")
	imageboxFirst = OffsetImage(FirstMoon, zoom=.5)
	xyMoonFirst = [First_2014_dates[5], 13]               # coordinates to position this image
	abMoonFirst = AnnotationBbox(imageboxFirst, xyMoonFirst,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFirst)

	# Add Text Full moon 2
	offsetboxFull2 = TextArea("Full Moon", minimumdescent=False)
	xyTextFull2 = [Full_2014_dates[5], 14.5]
	abTextFull2 = AnnotationBbox(offsetboxFull2, xyTextFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextFull2)

	# add Full moon 2 image 
	imageboxFull2 = OffsetImage(FullMoon, zoom=.5)
	xyMoonFull2 = [Full_2014_dates[5], 13]               # coordinates to position this image
	abMoonFull2 = AnnotationBbox(imageboxFull2, xyMoonFull2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonFull2)

	# Add Text Third
	offsetboxThird = TextArea("Third Quarter", minimumdescent=False)
	xyTextThird = [Third_2014_dates[5], 14.5]
	abTextThird = AnnotationBbox(offsetboxThird, xyTextThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextThird)

	# add Third moon image
	ThirdMoon = plt.imread("./Figures/ThreeQuarterMoonA.png")
	imageboxThird= OffsetImage(ThirdMoon, zoom=.5)
	xyMoonThird = [Third_2014_dates[5], 13]               # coordinates to position this image
	abMoonThird = AnnotationBbox(imageboxThird, xyMoonThird,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonThird)

	# Add Text New
	offsetbox2 = TextArea("New Moon", minimumdescent=False)
	xyTextNew2 = [New_2014_dates[6], 14.5]
	abTextNew2 = AnnotationBbox(offsetbox2, xyTextNew2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points")
	ax.add_artist(abTextNew2)

	# add New moon image
	NewMoon = plt.imread("./Figures/NewMoonA.png")
	imageboxNew2 = OffsetImage(NewMoon, zoom=.5)
	xyMoonNew2 = [New_2014_dates[6], 13]               # coordinates to position this image
	abMoonNew2 = AnnotationBbox(imageboxNew2, xyMoonNew2,
	    xybox=(30., -30.),
	    xycoords='data',
	    boxcoords="offset points",
	    frameon=False)                                  
	ax.add_artist(abMoonNew2)

	plt.title('Effects of position of the Moon relative to the Earth and Sun on the strength of the tides at Neah Bay')
	plt.style.use('ggplot')
	#Expand graph height
	plt.plot(Third_2014_dates[5],14.5)
	#Plot tide data
	plt.plot(subset["Date Time"], subset["Water Level"])
	# beautify the x-labels
	plt.gcf().autofmt_xdate()
	plt.xlabel("Time of Day (GMT)")
	plt.ylabel("Water Height (ft)")
	plt.draw()
	plt.show()

