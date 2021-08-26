import pandas as pd

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import classification_report
from sklearn.inspection import permutation_importance

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from sklearn.metrics import plot_roc_curve

def color_percent(floaty):
  "Input a normalized number between 0 and 1, and get it in string form colored according to percentage."
  if floaty >= .5:
    green = 200
    red = int(500 * (1 - floaty))
  else:
    red = 255
    green = int(400 * floaty)

  return f'\033[38;2;{red};{green};0m{floaty}\033[00m'


df = pd.read_csv('files/lending-club-subset.csv', skipinitialspace=True)

empty = ['member_id', 'next_pymnt_d']
df = df.drop(columns=empty)
weird = ['deferral_term', 'hardship_length', 'hardship_type']
df = df.drop(columns=weird)
constant = ['hardship_flag', 'policy_code', 'out_prncp_inv', 'out_prncp', 'pymnt_plan']
df = df.drop(columns=constant)
useless = ['url', 'id', 'emp_title', 'desc', 'title', 'zip_code']
df = df.drop(columns=useless)
leakage = ['fico_range_low', 'last_fico_range_high', 'last_fico_range_low']
df = df.drop(columns=leakage)

df['int_rate'] = df['int_rate'].str.strip('%').astype(float)
def numberinator(num):
    nums = '0123456789'
    numy = ''
    if type(num) == str:
        for char in num:
            if char in nums:
                numy += char

    if numy == '':
        numy = None
    else:
        numy = float(numy)

    return numy
df['emp_length'] = df['emp_length'].apply(numberinator)
df['revol_util'] = df['revol_util'].str.strip('%').astype(float)
df['term'] = df['term'].apply(numberinator)
grades = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
grader = lambda grade : grades[grade]
df['grade'] = df['grade'].apply(grader)
grader2 = lambda grade : grades[grade[0]] * int(grade[1])
df['sub_grade'] = df['sub_grade'].apply(grader2)

for x in df.columns:
    if df[x].nunique() > 100 and df[x].dtype == object:
        df = df.drop(columns=x)

# for x in df.columns:
#     if df[x].dtype == object:
#         df = df.drop(columns=x)


# print(df['emp_length'])
# print(df['title'].value_counts())


# for col in df.columns:
#     if df[col].nunique() < 3:
#         print('----------------------------------------------------------')
#         print(col)
#         print(f"{df[col].nunique()}/{len(df)}")
#         print()

# print(df['loan_status'].value_counts())


df.loc[df['home_ownership'] == 'RENT', 'renting'] = 1
df.loc[df['renting'] != 1, 'renting'] = 0
df = df.drop(columns='home_ownership')

df.to_csv('files/lending_edited.csv')

target = 'renting'
X = df.drop(target, axis=1)
y = df[target]

X_train, y_train = X.head(70000), y[:70000]
X_val, y_val = X[70000:85000], y[70000: 85000]
X_test, y_test = X[85000:], y[85000:]

# y_pred_b1 = [y_train.mean()] * len(y_train)
# print('Mean interest rate', y_train.mean())
# print('Baseline MAE', mean_absolute_error(y_train, y_pred_b1))

basAcc = y_train.value_counts(normalize=True).max()
print('\033[34mBaseline Accuracy:', color_percent(basAcc), end='\n\n')

# modelRF = make_pipeline(
#     OrdinalEncoder(),
#     SimpleImputer(strategy='mean'),
#     RandomForestClassifier(
#         n_jobs=-1,
#         random_state=42
#     )
# )
# modelRF.fit(X_train, y_train)

# print('\033[34mModel RandomForestClassifier\033[00m')
# print('Training Accuracy:', color_percent(modelRF.score(X_train, y_train)))
# print('Validation Accuracy:', color_percent(modelRF.score(X_val, y_val)), end='\n\n')


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


# modelGradient = make_pipeline(
#     OrdinalEncoder(),
#     SimpleImputer(strategy='mean'),
#     GradientBoostingClassifier(
#         random_state=42
#     )
# )
# modelGradient.fit(X_train, y_train)

# print('\033[34mModel GradientBoostingClassifier\033[00m')
# print('Training Accuracy:', color_percent(modelGradient.score(X_train, y_train)))
# print('Validation Accuracy:', color_percent(modelGradient.score(X_val, y_val)), end='\n\n')


# rfRoc = plot_roc_curve(modelRF, X_val, y_val)
# boostRoc = plot_roc_curve(modelRF, X_val, y_val, ax=rfRoc.ax_)
# # gradientRoc = plot_roc_curve(modelGradient, X_val, y_val, ax=rfRoc.ax_)
# plt.show()


report = classification_report(y_val, modelBoost.predict(X_val))
print(f"\033[31m{report}\033[00m\n")


permute = permutation_importance(
    modelBoost,
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
# importances.to_csv('files/important.csv')
print(importances.tail(20))


# coefs = modelBoost.named_steps['xgbclassifier'].coef_
# features = modelBoost.named_steps['ordinalencoder'].get_feature_names()
# feat_imp = pd.Series(coefs, index=features).sort_values(key=abs)
# feat_imp.to_csv('files/importances')