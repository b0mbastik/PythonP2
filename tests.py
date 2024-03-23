import unittest, io, sys, time, os
import data_refinement as dr, refined_graphs as rg, groupTable as gt

class TestRefinedData(unittest.TestCase):
    def setUp(self):
        self.df = dr.read_data('refined_census2011.csv')
        self.vf = dr.read_data('census_variables.csv')

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

    def test_get_sorted_columns(self):
        vc = self.df.Region.value_counts().sort_index()
        tup = rg.get_sorted_columns(self.df.Region, self.vf.Region)
        self.assertTrue(vc.compare(tup[0]).empty)
        self.assertTrue(self.vf.Region.dropna().compare(tup[1]).empty)
        self.assertRaises(ValueError, rg.get_sorted_columns, self.df.Region, self.vf.Industry)
        self.assertRaises(ValueError, rg.get_sorted_columns, self.df.Industry, self.vf.Region)

    def test_getTable(self):
        dt = gt.getTable(self.df, self.vf, "Occupation", "Approximated Social Grade")
        self.assertEqual(dt.columns.tolist(), self.vf["Approximated Social Grade"].dropna().values.tolist())
        self.assertEqual(dt.index.tolist() , self.vf["Occupation"].dropna().values.tolist())
        self.assertRaises(ValueError, gt.getTable, self.df, self.vf, "Not a variable", "Approximated Social Grade")
        self.assertRaises(ValueError, gt.getTable, self.df, self.vf, "Occupation", "Social Grade")
    