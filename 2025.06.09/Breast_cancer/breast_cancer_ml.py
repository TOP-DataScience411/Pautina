from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay, confusion_matrix, fbeta_score
from sklearn.model_selection import train_test_split
from pandas import DataFrame, Series
from pathlib import Path
from sys import path
from random import choice

dir_path = Path(path[0])

data_raw = load_breast_cancer()

def output_results(y_test, y_pred):
    conf_matr = confusion_matrix(y_test, y_pred)

    (TN, FP), (FN, TP) = conf_matr

    print(f'{mod}:\nConfusion Matrix\n {conf_matr}\n')

    accuracy = accuracy_score(y_test, y_pred)
    specificity = TN / (TN + FP)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    fbeta = fbeta_score(y_test, y_pred, beta = 0.5)

    print(
        f'{accuracy = :.1%}',
    f'{specificity = :.1%}',
    f'{precision = :.1%}',
    f'{recall = :.1%}',
    f'{f1 = :.1%}',
    f'{fbeta = :.1%}',
        sep= '\n',
        end= '\n\n'
    )

    color = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

    disp = ConfusionMatrixDisplay(conf_matr, display_labels=['Class 0', 'Class 1'])
    disp.plot(cmap= choice(color))
    plt.title(f'Breast cancer\n{mod}\nматрица ошибок')
    plt.savefig(dir_path / f'{mod}_conf_matrix.png')
    plt.close()

data = DataFrame(data_raw['data'], columns = data_raw['feature_names'])
target = Series(data_raw['target'])

data_all = DataFrame(
    dict(zip(
        data_raw['feature_names'],
        data_raw['data'].T
    ))
    | {'target' : data_raw['target']}
)

#нормализация данных
data_norm = (data - data.describe().loc['mean']) / data.describe().loc['std']

mean_0 = data_norm.loc[target == 0].mean().round(3)
mean_1 = data_norm.loc[target == 1].mean().round(3)

groupped = DataFrame({
    'mean 0': mean_0,
    'mean 1': mean_1,
    'diff': abs(mean_0 - mean_1)
}).sort_values(by = 'diff', ascending = False)

#fig = plt.figure(figsize = (8, 4))
#axs = fig.subplots()
#for var_name in groupped.index[:10]:
#    axs.clear()
#    axs.hist(
#        data_norm.loc[target == 0, var_name],
#        bins = 15,
#       alpha = 0.5,
#        label = '(0) злокачественная'
#    )
#    axs.hist(
#        data_norm.loc[target == 1, var_name],
#        bins = 15,
#        alpha = 0.5,
#       label = '(1) доброкачественная'
#    )
#    axs.set(xlabel = var_name, ylabel = 'Количество значений в интервале')
#   fig.savefig(dir_path / f'breast_cancer_{var_name}.png', dpi = 200)

X = data_norm.loc[:, groupped.index[:10]]

RS = 56

x_train, x_test, y_train, y_test = train_test_split(
    X, target,
    test_size = 0.2,
    random_state = RS
)

# Logistic Regression
from sklearn.linear_model import LogisticRegression

mod = 'LogisticRegression'

model_log_regr = LogisticRegression(max_iter = 1000, random_state = RS)

model_log_regr.fit(x_train, y_train)
y_pred_log_regr = model_log_regr.predict((x_test))


output_results(y_test, y_pred_log_regr)

# Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

mod = 'Bagging'

base_model = DecisionTreeClassifier(max_depth=5, min_samples_split=3, random_state = RS)
bagging = BaggingClassifier(base_model, n_estimators = 50, max_samples=0.8, random_state = RS)
bagging.fit(x_train, y_train)
y_pred_bagging = bagging.predict(x_test)

output_results(y_test, y_pred_bagging)

# Random forest
from sklearn.ensemble import RandomForestClassifier

mod = 'RandomForest'

model_random_forest = RandomForestClassifier(
    n_estimators = 100,
    max_depth = 5,
    min_samples_split=5,
    random_state = RS
)
model_random_forest.fit(x_train, y_train)
y_pred_random_forest = model_random_forest.predict(x_test)

output_results(y_test, y_pred_random_forest)

# Stacking
from sklearn.ensemble import StackingClassifier
from sklearn.svm import SVC

mod = 'Stacking' 

estimators = [
    ('dt', DecisionTreeClassifier(max_depth=5, random_state = RS)),
    ('svm', SVC(kernel='rbf', probability=True))
]
model_stacking = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(max_iter = 1000, random_state = RS),
    cv = 5,
    n_jobs=-1
)
model_stacking.fit(x_train, y_train)
y_pred_stacking = model_stacking.predict(x_test)
output_results(y_test, y_pred_stacking)


#LogisticRegression:
#Confusion Matrix
# [[44  2]
# [ 2 66]]
#
#accuracy = 96.5%
#specificity = 95.7%
#precision = 97.1%
#recall = 97.1%
#f1 = 97.1%
#fbeta = 97.1%
#
#Bagging:
#Confusion Matrix
# [[44  2]
# [ 4 64]]
#
#accuracy = 94.7%
#specificity = 95.7%
#precision = 97.0%
#recall = 94.1%
#f1 = 95.5%
#fbeta = 96.4%
#
#RandomForest:
#Confusion Matrix
# [[44  2]
# [ 3 65]]
#
#accuracy = 95.6%
#specificity = 95.7%
#precision = 97.0%
#recall = 95.6%
#f1 = 96.3%
#fbeta = 96.7%
#
#Stacking:
#Confusion Matrix
# [[45  1]
# [ 2 66]]
#
#accuracy = 97.4%
#specificity = 97.8%
#precision = 98.5%
#recall = 97.1%
#f1 = 97.8%
#fbeta = 98.2%
