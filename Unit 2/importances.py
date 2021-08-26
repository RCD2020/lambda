import pandas as pd

from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV

from sklearn.inspection import permutation_importance

import matplotlib.pyplot as plt

def color_percent(floaty):
  "Input a normalized number between 0 and 1, and get it in string form colored according to percentage."
  if floaty >= .5:
    green = 200
    red = int(500 * (1 - floaty))
  else:
    red = 255
    green = int(400 * floaty)

  return f'\033[38;2;{red};{green};0m{floaty}\033[00m'


df = pd.read_csv('files/lending_edited.csv')
df = df.drop(columns='mort_acc')


target = 'renting'
X = df.drop(target, axis=1)
y = df[target]

X_train, y_train = X.head(70000), y[:70000]
X_val, y_val = X[70000:85000], y[70000: 85000]
X_test, y_test = X[85000:], y[85000:]


basAcc = y_train.value_counts(normalize=True).max()
print('\n\033[34mBaseline Accuracy:', color_percent(basAcc), end='\n\n')


modelGradient = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    GradientBoostingClassifier(
        random_state=42
    )
)
modelGradient.fit(X_train, y_train)

print('\033[34mModel GradientBoostingClassifier\033[00m')
print('Training Accuracy:', color_percent(modelGradient.score(X_train, y_train)))
print('Validation Accuracy:', color_percent(modelGradient.score(X_val, y_val)), end='\n\n')


permute = permutation_importance(
    modelGradient,
    X_val,
    y_val,
    random_state=42
)
data = {
    'imp_mean': permute['importances_mean'],
    'imp_std': permute['importances_std']
}
importances = pd.DataFrame(data, index=X_val.columns)
importances = importances.sort_values(by='imp_mean', key=abs)
importances.to_csv('files/importances2.csv')
# print(importances.tail(20))

graphy = importances.tail(5)
plt.bar(x=graphy.index, height=graphy['imp_mean'])
plt.show()