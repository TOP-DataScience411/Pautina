from pathlib import Path
from sys import path
from pandas import read_csv, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, fbeta_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


dir_path = Path(path[0])

data_all = read_csv(dir_path / 'wilt.csv')
data_all['class'] = data_all['class'].replace({'w':0, 'n':1})
#print(data_all.info())

data = data_all.iloc[:, 1:]
target = data_all['class']
#print(data)

#print(target.value_counts())
#0 - больные деревья
#1 - другое покрытие

data_norm = (data - data.describe().loc['mean']) / data.describe().loc['std']
#print(data_norm)

#до удаления выбросов
corr_matrix = data_all.corr('spearman')
#print(corr_matrix)

# после удаления выбросов
#for col in data.columns:
#    data[col] = mstats.winsorize(data[col], limits=[0.05, 0.05])

#corr_matrix = data.corr('spearman')
#print(corr_matrix)

plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.savefig(dir_path / 'boxplot_wilt.png')

x_train, x_test, y_train, y_test = train_test_split(
    data_norm,
    target,
    test_size = 0.3,
    random_state = 1,
    stratify=target
)

model = LogisticRegression(class_weight='balanced')

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
#print(y_test.value_counts())

conf_matr = confusion_matrix(y_test, y_pred)

print(conf_matr)

(TN, FP), (FN, TP) = conf_matr

accuracy = (TN + TP) / (TN + FP + FN + TP)

specificity = TN / (TN + FP)
precision = TP / (FP + TP)
recall = TP / (FN + TP)

f1 = 2 * precision * recall / (precision + recall)
fbeta = fbeta_score(y_test, y_pred, beta = 0.1)

print(
    f'{accuracy = :.1%}',
f'{specificity = :.1%}',
f'{precision = :.1%}',
f'{recall = :.1%}',
f'{f1 = :.1%}',
f'{fbeta = :.1%}',
    sep= '\n'
)

#[[  71    7]
# [  93 1281]]
#accuracy = 93.1%
#specificity = 91.0%
#precision = 99.5%
#recall = 93.2%
#f1 = 96.2%
#fbeta = 99.4%
#>>>