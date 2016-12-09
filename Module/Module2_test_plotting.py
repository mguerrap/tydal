import unittest
import pandas
import module2_utils as tides


class TestDataPlotting(unittest.TestCase):

    def testGoogleMapworks(self):
        # Check that I can load the google map of the stations
        stamap = tides.add_station_maps()
        self.assertIs(type(stamap), gmaps.maps.Map)

    def testCreateTideDataset(self):
        # Generate the tidal dataset
        NB = tides.load_Neah_Bay('../Data/')
        PA = tides.load_Port_Angeles('../Data/')
        PT = tides.load_Port_Townsend('../Data/')
        # Create the XArray dataset
        Tides = tides.create_tide_dataset(NB, PA, PT)
        # Check that it is an xarray DataSet
        self.assertIs(type(Tides), xarray.core.dataset.Dataset)

    def testTideDatasetfails(self):
    	# Generate the tidal dataset
        NB = tides.load_Neah_Bay('../Data/')
        PA = tides.load_Port_Angeles('../Data/')
        PT = None
        # Don't load all of the Data Arrays
        Tides = tides.create_tide_dataset(NB, PA, None)
        self.assertTrue(Tides == None)
