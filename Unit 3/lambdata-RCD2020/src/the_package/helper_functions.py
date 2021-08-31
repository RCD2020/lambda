import pandas as pd


class DataFrameInfo:

    def __init__(self, df):
        self.null = df.isnull().sum().sum()
        self.length = len(df)
        self.shape = df.shape


def null_count(df):
    "Takes a pandas.DataFrame and returns the total null values."

    return df.isnull().sum().sum()


def null_count2(df):
    "Takes a pandas.DataFrame and returns the total null values."

    info = DataFrameInfo(df)

    return info.null


def split_dates(date_series):
    "Takes a pandas.Series filled with dates in the 'MM/DD/YYYY' format and returns a pandas.DataFrame with the dates split into three columns."

    dates = {
        'month': [],
        'day': [],
        'year': []
    }

    for x in date_series:
        points = x.split('/')

        dates['month'].append(points[0])
        dates['day'].append(points[1])
        dates['year'].append(points[2])

    return pd.DataFrame(dates)
