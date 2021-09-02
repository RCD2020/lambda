import pandas as pd


class DataFrameInfo:
    """Simple class that pulls some basic information from a pandas.DataFrame.
    
    1. null: total null values in DataFrame
    2. length: how long the DataFrame is
    3. shape: shape of the DataFrame"""

    def __init__(self, df: pd.DataFrame):
        """Initiates DataFrameInfo"""

        self.null = df.isnull().sum().sum()
        self.length = len(df)
        self.shape = df.shape


def null_count(df: pd.DataFrame):
    """Takes a pandas.DataFrame, and returns the total null count in that dataframe."""

    return df.isnull().sum().sum()


def null_count2(df: pd.DataFrame):
    """Takes a pandas.DataFrame, and returns the total null count in that dataframe.
    
    A secondary null_count function that utilizes the DataFrameInfo class to calculate the null count.
    It is slower than null_count, but oh well. Assignments be like"""

    info = DataFrameInfo(df)

    return info.null


def split_dates(date_series: pd.Series):
    """Takes a pandas.Series filled with dates in the 'MM/DD/YYYY' format.
    
    Returns a pandas.DataFrame with the dates split into three columns; month, day, and year."""
    "Takes a pandas.Series filled with dates in the 'MM/DD/YYYY' format and returns a pandas.DataFrame with the dates split into three columns."

    dates = {
        'month': [],
        'day': [],
        'year': []
    }

    for x in date_series:
        points = x.split('/')

        dates['month'].append(int(points[0]))
        dates['day'].append(int(points[1]))
        dates['year'].append(int(points[2]))

    return pd.DataFrame(dates)