from pathlib import Path
from sys import path

from matplotlib import pyplot as plt
from numpy import array, linspace, load as load_npz, std, where
from sklearn.linear_model import RANSACRegressor
from sklearn.metrics import mean_squared_error


script_dir = Path(path[0])
data_path = load_npz(script_dir / 'data1.npz')

#print(list(data.keys()))

with data_path as data:
  x, y = array(data['x']), array(data['y'])


#print(x.shape, y.shape)
#print("Стандартные отклонения:", round(std(x), 2), round(std(y), 2))

plt.scatter(x, y, color='blue')
plt.title('Scatter Plot')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.savefig(script_dir / f'Scatter_plot.png')
plt.close()

#Сильнейшее влияние на изменеие кластеров оказывает параметр residual_threshold
thresholds = linspace(0.1, 1, 10)
fig, axs = plt.subplots(2, 5, figsize=(20, 8))
fig.suptitle("Влияние residual_threshold на RANSAC", fontsize=18)


for i, threshold in enumerate(thresholds):
    ax = axs[i // 5, i % 5]
    model = RANSACRegressor(min_samples=2, residual_threshold=threshold, max_trials=100, random_state=42)
    model.fit(x.reshape(-1, 1), y)

    inlier_mask = model.inlier_mask_
    outlier_mask = ~inlier_mask

    ax.scatter(x[inlier_mask], y[inlier_mask], color='blue', alpha=0.7, s=8, label='Линейный кластер')
    ax.scatter(x[outlier_mask], y[outlier_mask], color='red', alpha=0.7, s=8, label='Зигзагообразный кластер')

    line_x = array([x.min(), x.max()])
    line_y = model.predict(line_x.reshape(-1, 1))
    ax.plot(line_x, line_y, color='green', linewidth=2, label='RANSAC модель')

    ax.set_title(f"threshold = {threshold:.2f}")
    ax.legend()
    ax.grid(True)
    
plt.tight_layout()
plt.savefig(script_dir / 'Влияние residual_threshold на RANSAC.png', dpi=300)
plt.close()

model = RANSACRegressor(min_samples=2, residual_threshold=0.4, max_trials=100, random_state=42)
model.fit(x.reshape(-1, 1), y)

inlier_mask = model.inlier_mask_
labels = where(inlier_mask, 0, 1) 


plt.figure(figsize=(10, 8))

plt.scatter(x[labels == 0], y[labels == 0], c='blue', s=30, 
            alpha=0.7, label=f'Линейный кластер (n={sum(labels == 0)})')
plt.scatter(x[labels == 1], y[labels == 1], c='red', s=30, 
            alpha=0.7, label=f'Зигзагообразный кластер (n={sum(labels == 1)})')

line_X = linspace(min(x), max(x), 100)
line_y = model.predict(line_X.reshape(-1, 1))
plt.plot(line_X, line_y, 'g-', linewidth=3, 
         label=f'Линейная модель: y = {model.estimator_.coef_[0]:.2f}x + {model.estimator_.intercept_:.2f}')

plt.title('Финальное разделение на кластеры')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.savefig(script_dir / f'Финальное разделение на кластеры.png')
plt.close()