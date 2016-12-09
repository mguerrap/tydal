import unittest
import module3_utils as m3
import tide_utils as tu


#class TestCurrentModel(unittest.TestCase):

#class TestFerryImport(unittest.TestCase):

class TestFerryPloting(unittest.TestCase):

    def setUp(self):
        # import tides
        pt_tide = tu.load_Port_Townsend('../Data/')
        self.pt_tide = pt_tide['Water Level']

        # import and clean ferry data
        URL1 = ('http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/' +
                'Salish_L1_STA.ncml')
        ferry = m3.ferry_data_download(URL1)
        ferryQC = m3.ferry_data_QC(ferry)
        self.ferryQC = m3.count_route_num(ferry)

        # define dates
        self.start_time = '2016-10-01'
        self.end_time = '2016-11-01'
        self.time_index = 100

    # Test tide plotting subfunction
    def test_plt_tide(self):
        # Assert time_index is too large
        time_index = 50000
        with self.assertRaises(ValueError):
            m3.plt_tide(self.pt_tide, time_index,
                        self.start_time, self.end_time)


    # # Test tide plotting subfunction
    # def test_plt_ferry_and_tide(self):
    #     URL1='http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/Salish_L1_STA.ncml'
    #     ferry=m3.ferry_data_download(URL1)
    #     ferryQC= m3.ferry_data_QC(ferry,6.5,4,4)

    #     ferryQC = m3.count_route_num(ferryQc)

    #     # define dates
    #     start = '2016-10-01'
    #     end = '2016-11-01'
    #     index = 10
    #     pt_tide = tu.load_Port_Townsend('../Data/')
    #     pt_tide = pt_tide['Water Level']

    #     m3.plt_ferry_and_tide(ferryQc, pt_tide, index, start, end)

    #     self.assertTrue(1 == 1)

if __name__ == '__main__':
    unittest.main()