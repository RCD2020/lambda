import pandas as pd

df = pd.read_csv('files/lending-club-subset.csv')
print(df.shape)
df2 = pd.read_csv('files/lending_edited.csv')
print(df2.shape)