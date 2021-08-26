import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('files/importances2.csv', index_col=0)
graphy = df.tail(5)
plt.bar(x=graphy.index, height=graphy['imp_mean'])
plt.show()