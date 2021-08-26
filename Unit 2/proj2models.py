import pandas as pd

from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

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


target = 'renting'
X = df.drop(target, axis=1)
y = df[target]

X_train, y_train = X.head(70000), y[:70000]
X_val, y_val = X[70000:85000], y[70000: 85000]
X_test, y_test = X[85000:], y[85000:]


basAcc = y_train.value_counts(normalize=True).max()
print('\n\033[34mBaseline Accuracy:', color_percent(basAcc), end='\n\n')


modelLinear = make_pipeline(
  OrdinalEncoder(),
  SimpleImputer(strategy='mean'),
  RidgeClassifier(
    random_state=42
  )
)
modelLinear.fit(X_train, y_train)

print('\033[34mModel RidgeClassifier\033[00m')
print('Training Accuracy:', color_percent(modelLinear.score(X_train, y_train)))
print('Validation Accuracy:', color_percent(modelLinear.score(X_val, y_val)), end='\n\n')


modelRF = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='mean'),
    RandomForestClassifier(
        n_jobs=-1,
        random_state=42
    )
)
modelRF.fit(X_train, y_train)

print('\033[34mModel RandomForestClassifier\033[00m')
print('Training Accuracy:', color_percent(modelRF.score(X_train, y_train)))
print('Validation Accuracy:', color_percent(modelRF.score(X_val, y_val)), end='\n\n')


modelBoost = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='mean'),
    XGBClassifier(
        random_state=42,
        eval_metric='merror',
        use_label_encoder=False
    )
)
modelBoost.fit(X_train, y_train)

print('\033[34mModel XGBClassifier\033[00m')
print('Training Accuracy:', color_percent(modelBoost.score(X_train, y_train)))
print('Validation Accuracy:', color_percent(modelBoost.score(X_val, y_val)), end='\n\n')


modelGradient = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='mean'),
    GradientBoostingClassifier(
        random_state=42
    )
)
modelGradient.fit(X_train, y_train)

print('\033[34mModel GradientBoostingClassifier\033[00m')
print('Training Accuracy:', color_percent(modelGradient.score(X_train, y_train)))
print('Validation Accuracy:', color_percent(modelGradient.score(X_val, y_val)), end='\n\n')
