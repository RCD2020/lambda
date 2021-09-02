# lambdata-RCD2020
### Lambda Helper Functions Package

---

## Classes

### DataFrameInfo

**DataFrameInfo(df: pandas.DataFrame)**

Simple class that pulls some basic information from a pandas.DataFrame

1. null: total null values in DataFrame
2. length: how long the DataFrame is
3. shape: shape of teh DataFrame

---

## Functions

### null_count

**null_count(df: pandas.DataFrame)**

Takes a pandas.DataFrame, and returns the total null count in that dataframe

### null_count2

**null_count2(df: pandas.DataFrame)**

Takes a pandas.DataFrame, and returns th total null count in that dataframe.
        
A secondary null_count function that utilizes the DataFrameInfo class to calculate the null count.
It is slower than null_count, but oh well. Assignments be like

### split_dates

**split_dates(date_series: pandas.Series)**

Takes a pandas.Series filled with dates in the 'MM/DD/YYYY' format.

Returns a pandas.DataFrame with the dates split into three columns; month, day, and year.

