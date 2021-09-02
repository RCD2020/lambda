import pytest
import pandas as pd
from helper_functions import *

null3 = pd.DataFrame({
    0: [0, 1, None],
    1: [4, None, 6],
    2: [None, 8, 9]
})

no_null = pd.DataFrame({
    0: [1, 2, 3]
})

dates = pd.Series([
    '01/28/2001',
    '07/04/1776',
    '09/02/2021'
])

dates_correct = pd.DataFrame({
    'month': [1, 7, 9],
    'day': [28, 4, 2],
    'year': [2001, 1776, 2021]
})

def test_class():
    assert DataFrameInfo(null3).null == 3
    assert DataFrameInfo(no_null).null == 0

def test_null1():
    assert null_count(null3) == 3
    assert null_count(no_null) == 0

def test_null2():
    assert null_count2(null3) == 3
    assert null_count2(no_null) == 0

def test_split():
    assert split_dates(dates).equals(dates_correct)