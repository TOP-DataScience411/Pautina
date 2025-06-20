from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, fbeta_score, f1_score, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from pandas import read_csv
from pathlib import Path
from sys import path

from random import choice


dir_path = Path(path[0])

data_all = read_csv(dir_path  / 'data_banknote_authentication.csv')

# 0 - поддельная - отрицательный
# 1 - подлинная - положительный

def output_results(y_test, y_pred):
    conf_matr = confusion_matrix(y_test, y_pred)

    (TN, FP), (FN, TP) = conf_matr

    print(f'{mod}:\nМатрица ошибок\n{conf_matr}\n')

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
    plt.title(f'{mod}\nматрица ошибок')
    plt.savefig(dir_path / f'{mod}_conf_matrix.png')
    plt.close()

RS = 100

x_train, x_test, y_train, y_test = train_test_split(
    data_all.loc[:, ['variance',  'skewness',  'curtosis',  'entropy']],
    data_all['class'],
    test_size = 1/3,
    random_state = RS
)
y_test.value_counts()

# Logistic Regression
from sklearn.linear_model import LogisticRegression

mod = 'LogisticRegression'

model_log_regr = LogisticRegression(random_state = RS)

model_log_regr.fit(x_train, y_train)
y_pred_log_regr = model_log_regr.predict((x_test))


output_results(y_test, y_pred_log_regr)

# Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

mod = 'Bagging'

base_model = DecisionTreeClassifier(max_depth=5, min_samples_split=3, random_state = RS)
bagging = BaggingClassifier(base_model, n_estimators=50, random_state = RS)
bagging.fit(x_train, y_train)
y_pred_bagging = bagging.predict(x_test)

output_results(y_test, y_pred_bagging)

# Random forest
from sklearn.ensemble import RandomForestClassifier

mod = 'RandomForest'

model_random_forest = RandomForestClassifier(
    n_estimators = 100,
    max_depth = 10,
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
    final_estimator=LogisticRegression(random_state = RS),
    cv = 5,
    n_jobs=-1
)
model_stacking.fit(x_train, y_train)
y_pred_stacking = model_stacking.predict(x_test)

output_results(y_test, y_pred_stacking)


#LogisticRegression:
#Матрица ошибок
#[[257   4]
# [  0 197]]
#
#accuracy = 99.1%
#specificity = 98.5%
#precision = 98.0%
#recall = 100.0%
#f1 = 99.0%
#fbeta = 98.4%
#
#Bagging:
#Матрица ошибок
#[[260   1]
# [  4 193]]
#
#accuracy = 98.9%
#specificity = 99.6%
#precision = 99.5%
#recall = 98.0%
#f1 = 98.7%
#fbeta = 99.2%
#
#RandomForest:
#Матрица ошибок
#[[260   1]
# [  0 197]]
#
#accuracy = 99.8%
#specificity = 99.6%
#precision = 99.5%
#recall = 100.0%
#f1 = 99.7%
#fbeta = 99.6%
#
#Stacking:
#Матрица ошибок
#[[261   0]
# [  0 197]]
#
#accuracy = 100.0%
#specificity = 100.0%
#precision = 100.0%
#recall = 100.0%
#f1 = 100.0%
#fbeta = 100.0%
#