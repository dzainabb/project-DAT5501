import unittest
from src.support_figure import load_data


def test_load_fertility_data(filepath='data/fertility_rate.csv'):
    df= load_data(filepath)
    assert not df.empty, "Fertility data should not be empty"

def test_columns_fertility_data(filepath='data/fertility_rate.csv'):
    df= load_data(filepath)
    assert 'Fertility rate - Sex: all - Age: all - Variant: estimates' in df.columns
    assert 'Year' in df.columns
    assert 'Entity' in df.columns
    assert 'Code' in df.columns

def test_year_data_type(filepath='data/fertility_rate.csv'):
    df= load_data(filepath)
    assert df['Year'].dtype == 'int', "Year column should be of type interger"



    