import unittest, io, sys, time, os
from data_refinement import RefineData

class TestRefinedData(unittest.TestCase):
    def setUp(self):
        self.df = RefineData.read_data('refined_census2011.csv')

    def test_read_data(self):
        self.assertTrue(self.df.compare(RefineData.read_data('refined_census2011.csv')).empty)
        self.assertRaises(FileNotFoundError, RefineData.read_data, 'census2010.csv')

    def test_refine_dataset(self):
        df = RefineData.read_data('census2011.csv')
        self.assertTrue(self.df.compare(RefineData.refine_dataset(df)).empty)

    def test_save_refined_data(self):
        RefineData.save_refined_data(self.df, 'refined_testData.csv')
        self.assertTrue(self.df.compare(RefineData.read_data('refined_testData.csv')).empty)
        os.remove('refined_testData.csv')