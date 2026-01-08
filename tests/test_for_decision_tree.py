#aims to check if the data is loaded and cleaned properly for decision tree model training

import unittest
import pandas as pd

from src.decision_tree import load_data

# Unit test class for decision tree data loading and cleaning
class TestDecisionTreeData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the data once for all tests
        cls.path = 'data/combined_data.csv'
        cls.data = load_data(cls.path)

    def test_data_not_empty(self):
    # Check if the loaded data is not empty
        self.assertFalse(
            self.data.empty,
            "The loaded data should not be empty."
        )
    def test_only_2023_data(self):
    # Check if all data is from the year 2023
        self.assertEqual(
            self.data['Year'].nunique(),
            1,
            "The data should only contain entries from only the  year 2023."
        )
        self.assertEqual(
            self.data['Year'].iloc[0],
            2023,
            "The data should only contain entries from the year 2023."
        )
    def test_required_columns(self):
        # Check if all required columns are present
        expected_columns = {
            'Country Name',
            'Country Code',
            'Year',
            'Fertility Rate',
            'Female employment (%)',
            'GDP per capita',
            'Urban Population (%)'
        }
        self.assertTrue(
            expected_columns.issubset(set(self.data.columns)),
            "The data should contain all required columns."
        )
    def test_no_missing(self):
        # Check if there are no missing values in the data
        self.assertFalse(
            self.data.isnull().values.any(),
            "The data should not contain any missing values."
        )

if __name__ == '__main__':
    unittest.main()


