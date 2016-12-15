import unittest
import os
import numpy as np
import pandas as pd
import module1_utils as mod1


class TestMod1(unittest.TestCase):
    """
    Creates a class to test the functions in module 1 utilities.
    """

    def test_trim_data(self):
        """
        This function tests the "trim_data" function.
        """
        df = pd.DataFrame({"A": [1, 2, 3, 4],
                           "Date Time": pd.date_range('1/1/2014', periods=4)})
        result = pd.DataFrame({"A": [2, 3],
                               "Date Time": pd.date_range('1/2/2014',
                                                          periods=2)})
        self.assertEqual(mod1.trim_data(df, "2014-01-02", "2014-01-03").shape,
                         result.shape)


if __name__ == "__main__":
    unittest.main()
