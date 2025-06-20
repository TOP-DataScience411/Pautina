from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, median_absolute_error, max_error
from matplotlib import pyplot as plt
from matplotlib import rcParams
from numpy import sqrt

from pathlib import Path
from sys import path

rcParams['text.color'] = 'black'

dir_path = Path(path[0])
data_path = dir_path / 'boston.csv'
data = read_csv(data_path, comment = '#')

def output_results(y_test, y_pred, model_name=None):
    metrics = {
        'R²': r2_score(y_test, y_pred),
        'MSE': mean_squared_error(y_test, y_pred),
        'RMSE': sqrt(mean_squared_error(y_test, y_pred)),
        'MAE': mean_absolute_error(y_test, y_pred),
        'MedAE': median_absolute_error(y_test, y_pred),
        'MaxError': max_error(y_test, y_pred)
    }
    print(f'\n{mod}:\n')
    for name, value in metrics.items():
        print(f'{name}: {value:.2f}')
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(y_test, y_pred, alpha=0.5, label='Предсказания')
    ax.plot([y_test.min(), y_test.max()], 
            [y_test.min(), y_test.max()], 
            'k--', lw=2)
    ax.set_title(f'{mod}\nРеальные vs Предсказанные значения')
    ax.set_xlabel('Реальные значения')
    ax.set_ylabel('Предсказанные значения')
    ax.legend()
    ax.grid(True)
    plt.savefig(dir_path / f'{mod}_real_vs_pred.png', bbox_inches='tight')
    plt.close()

corr_matrix_pearson = data.corr('pearson').round(2)
corr_matrix_spearman = data.corr('spearman').round(2)

#fig = plt.figure(figsize = (56, 56))
#axs = fig.subplots(14, 14)

#for i, col1 in enumerate(data):
#    for j, col2 in enumerate(data):
#        if i > j:
#            axs[i][j].scatter(data[col1], data[col2], s = 7)
#            axs[i][j].text(
#                data[col1].max(),
#                data[col2].max(),
#                f'p = {corr_matrix_pearson.loc[col1, col2]}\n'
#                f's = {corr_matrix_spearman.loc[col1, col2]}',
#                horizontalalignment = 'right',
#                verticalalignment = 'top',
#            )
#            axs[i][j].set(
#                xticks = [],
#                yticks = [],
#                xlabel = col1,
#                ylabel = col2,
#            )
#        else:
#            axs[i][j].axis('off')
#fig.savefig(dir_path / 'boston_14x14_graphs.png', dpi = 300)

data_out = data.loc[data['MEDV'] != data['MEDV'].max()]

#print(
#    'после отбраковки выбросов',
#    data_out.corr('pearson').round(2),
#   data_out.corr('spearman').round(2),
#    sep = '\n\n',
#    end = '\n\n'
#)

X = data_out.loc[:, ['CRIM', 'INDUS', 'RM', 'AGE', 'LSTAT']]
Y = data_out['MEDV']

test_rate = 0.2
test_len = int(X.shape[0] * test_rate)
train_len = X.shape[0] - test_len

RS = 17

x_train, x_test, y_train, y_test = train_test_split(
        X, Y,
        test_size = 0.2,
        random_state = RS,
    )


# Linear Regression
from sklearn.linear_model import LinearRegression

mod = 'LinearRegression'

model_lin_regr = LinearRegression()
model_lin_regr.fit(x_train, y_train)
y_pred_lin_regr = model_lin_regr.predict(x_test)

output_results(y_test, y_pred_lin_regr)

# Bagging
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor

mod = 'Bagging'

base_model = DecisionTreeRegressor(max_depth=7, min_samples_split=10, random_state = RS)
bagging = BaggingRegressor(base_model, n_estimators = 100, max_samples=0.7, max_features = 0.7, n_jobs = - 1, random_state = RS)
bagging.fit(x_train, y_train)
y_pred_bagging = bagging.predict(x_test)

output_results(y_test, y_pred_bagging)

# Random forest
from sklearn.ensemble import RandomForestRegressor

mod = 'RandomForest'

model_random_forest = RandomForestRegressor(
    n_estimators = 200,          
    max_depth = 10,           
    min_samples_split = 5,       
    min_samples_leaf = 2,        
    max_features = 1,       
    random_state = RS,
    n_jobs = -1                  
)
model_random_forest.fit(x_train, y_train)
y_pred_random_forest = model_random_forest.predict(x_test)

output_results(y_test, y_pred_random_forest)

# Stacking
from sklearn.ensemble import StackingRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

mod = 'Stacking' 

estimators = [
    ('rf', RandomForestRegressor(n_estimators = 200,
    max_depth = 10,
    max_features = 1,
    min_samples_split = 5,
    random_state = RS)),
    ('svr', SVR(kernel='linear')),
]

model_stacking = StackingRegressor(
    estimators=estimators,
    final_estimator=LinearRegression(),
    cv=5
)
model_stacking.fit(x_train, y_train)
y_pred_stacking = model_stacking.predict(x_test)

output_results(y_test, y_pred_stacking)


#LinearRegression:
#
#R²: 0.78
#MSE: 10.37
#RMSE: 3.22
#MAE: 2.58
#MedAE: 2.09
#MaxError: 9.79
#
#Bagging:
#
#R²: 0.84
#MSE: 7.74
#RMSE: 2.78
#MAE: 2.11
#MedAE: 1.72
#MaxError: 9.36
#
#RandomForest:
#
#R²: 0.85
#MSE: 6.89
#RMSE: 2.62
#MAE: 2.01
#MedAE: 1.82
#MaxError: 8.01
#
#Stacking:
#
#R²: 0.84
#MSE: 7.68
#RMSE: 2.77
#MAE: 2.14
#MedAE: 1.64
#MaxError: 9.14#