import unittest
import pandas
import tydal.module2_utils as tides


class TestModule2(unittest.TestCase):

    # Testing the station map
    def testNeahBayfails(self):
        # Check that the data can't be loaded
        NB = tides.load_Neah_Bay('Bad Directory')
        self.assertTrue(NB == None)

    def testNeahBayloads(self):
        # Load the NeahBay data
        NB = tides.load_Neah_Bay('../Data/')
        self.assertIs(type(NB), pandas.core.frame.DataFrame)

    def testPortAngelesfails(self):
        # Check that the Port Angeles can't be loaded
        PA = tides.load_Port_Angeles('Bad Directory')
        self.assertTrue(PA == None)

    def testPortAngelesloads(self):
        # Check that the Port Angeles will load
        PA = tides.load_Port_Angeles('../Data/')
        self.assertIs(type(PA), pandas.core.frame.DataFrame)

    def testPortTownsendfails(self):
        PT = tides.load_Port_Townsend('Bad Directory')
        self.assertTrue(PT == None)

    def testPortTownsendloads(self):
        PT = tides.load_Port_Townsend('../Data/')
        self.assertIs(type(PT), pandas.core.frame.DataFrame)

    def testCreateTideDataset(self):
        import xarray
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

    def testPlotTideDataIndexFails(self):
        NB = tides.load_Neah_Bay('../Data/')
        PA = tides.load_Port_Angeles('../Data/')
        PT = tides.load_Port_Townsend('../Data/')
        # Create the XArray dataset
        Tides = tides.create_tide_dataset(NB, PA, PT)
        # Test that time selection is below available times
        self.assertRaises(IndexError, tides.plot_tide_data, Tides,
                          '2012', '2013')
        # Test when time selection is above time range
        self.assertRaises(IndexError, tides.plot_tide_data, Tides,
                          '2017', '2018')
        # Test when the times are switched
        self.assertRaises(IndexError, tides.plot_tide_data, Tides,
                          '2016', '2015')


if __name__ == '__main__':
    unittest.main()
