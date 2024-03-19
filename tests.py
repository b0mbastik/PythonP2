import unittest, io, sys, time, os
import data_refinement as dr 

class TestRefinedData(unittest.TestCase):
    def setUp(self):
        self.df = dr.read_data('refined_census2011.csv')

    def test_read_data(self):
        self.assertTrue(self.df.compare(dr.read_data('refined_census2011.csv')).empty)
        self.assertRaises(FileNotFoundError, dr.read_data, 'census2010.csv')

    def test_refine_dataset(self):
        df = dr.read_data('census2011.csv')
        self.assertTrue(self.df.compare(dr.refine_dataset(df)).empty)

    def test_save_refined_data(self):
        dr.save_refined_data(self.df, 'refined_testData.csv')
        self.assertTrue(self.df.compare(dr.read_data('refined_testData.csv')).empty)
        os.remove('refined_testData.csv')