import unittest
import module3_utils as m3
import tide_utils as tu
import numpy as np

class TestCurrentModel(unittest.TestCase):

    def test_currents_bad_alpha(self):
        # Assert when alpha is less than 0 
        with self.assertRaises(ValueError):
            m3.tidal_currents(12.42, 1, 1, -10)
    def test_currents_bad_a1(self):
        # Assert when alpha is less than 0 
        with self.assertRaises(ValueError):
            m3.tidal_currents(12.42, -1, 1, 10)
    def test_currents_bad_a2(self):
        # Assert when alpha is less than 0 
        with self.assertRaises(ValueError):
            m3.tidal_currents(12.42, 1, -1, 10)

class TestFerryImport(unittest.TestCase):

    def testFerryDataDownload_Good(self):
        URL1 = ('http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/' +
                'Salish_L1_STA.ncml')
        result = m3.ferry_data_download(URL1)
        self.assertTrue(result[1])
        explanation = 'Good URL, File downloaded'
        self.assertEqual(result[2],explanation)

    def testFerryQC_error(self):
        ferry = np.nan
        # Assert when ferry is a nan value 
        with self.assertRaises(ValueError):
            m3.ferry_data_QC(ferry,6.5,5,5)

    # def testFerryQC_good(self):
    #     URL1 = ('http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/' +
    #             'Salish_L1_STA.ncml')
    #     [ferry, status, message] = m3.ferry_data_download(URL1)
    #     result = m3.ferry_data_QC(ferry,6.5,5,5)
    #     self.assertTrue(result[1])

# class TestFerryPloting(unittest.TestCase):

#     def setUp(self):
#         # import tides
#         pt_tide = tu.load_Port_Townsend('../Data/')
#         self.pt_tide = pt_tide['Water Level']

#         # import and clean ferry data
#         URL1 = ('http://107.170.217.21:8080/thredds/dodsC/Salish_L1_STA/' +
#                 'Salish_L1_STA.ncml')
#         ferry = m3.ferry_data_download(URL1)
#         ferryQC = m3.ferry_data_QC(ferry)
#         self.ferryQC = m3.count_route_num(ferry)

#         # define dates
#         self.start_time = '2016-10-01'
#         self.end_time = '2016-11-01'
#         self.time_index = 100

#     # Test tide plotting subfunction
#     def test_plt_tide(self):
#         # Assert time_index is too large
#         time_index = 50000
#         with self.assertRaises(ValueError):
#             m3.plt_tide(self.pt_tide, time_index,
#                         self.start_time, self.end_time)

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
        (ferry, file_downloaded, explanation) = m3.ferry_data_download(URL1)
        # ferryQC = m3.ferry_data_QC(ferry,6.5,4,4)
        self.ferryQC = m3.count_route_num(ferry)
        # define dates
        self.start_time = '2016-10-01'
        self.end_time = '2016-11-01'
        self.time_index = 50000

    # Test tide plotting subfunction
    def test_plt_tide(self):
        # Assert time_index is too large
        with self.assertRaises(ValueError):
            m3.plt_tide(self.pt_tide, self.time_index,
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
    # Test tide plotting subfunction
    def test_plt_tide(self):
        # Assert time_index is too large
        time_index = 50000
        with self.assertRaises(ValueError):
            m3.plt_tide(self.pt_tide, time_index,
                        self.start_time, self.end_time)

    def test_plt_tide_and_ferry(self):
        crossing_index = 100000
        with self.assertRaises(ValueError):
            m3.plt_ferry_and_tide(self.ferryQC, self.pt_tide,
                                  crossing_index, self.start_time,
                                  self.end_time)

    def test_count_route_num(self):
        ferry_out = m3.count_route_num(self.ferryQC)
        self.assertTrue(hasattr(ferry_out, 'xing_num'))
        # self.assertTrue(min(ferry_out['xing_num']) == -9)
        # self.assertTrue(max(ferry_out['xing_num']) > 0)
if __name__ == '__main__':
    unittest.main()