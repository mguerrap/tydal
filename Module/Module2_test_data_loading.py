import unittest
import module2_utils as tides

class TestDataLoading(unittest.TestCase):


    # Testing the station map
    def testNeahBayfails(self):
        # Check that the data can't be loaded
        self.assertRaises(FileNotFoundError,
                          tides.load_Neah_Bay('Bad Directory'))


    def testNeahBayloads(self):
        # Load the NeahBay data
        NB = tides.load_Neah_Bay('../Data/')
        self.assertTrue(type(NB),pandas.core.frame.DataFrame)


    def testPortAngelesfails(self):
        # Check that the Port Angeles can't be loaded
        self.assertRaises(FileNotFoundError,
                          tides.load_Port_Angeles('Bad Directory'))


    def testPortAngelesloads(self):
        # Check that the Port Angeles will load
        PA = tides.load_Port_Angeles('../Data/')
        self.assertTrue(type(PA),pandas.core.frame.DataFrame)


if __name__ == '__main__':
    unittest.main()