from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from task_1 import x, y, inlier_mask, line_X, script_dir


x_inliers = x[inlier_mask].reshape(-1, 1)
y_inliers = y[inlier_mask]


model = LinearRegression()
model.fit(x_inliers, y_inliers)


y_pred = model.predict(x_inliers)


mse = mean_squared_error(y_inliers, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_inliers, y_pred)
r2 = r2_score(y_inliers, y_pred)


plt.figure(figsize=(10, 8))
plt.scatter(x_inliers, y_inliers, color='blue', alpha=0.8, label='Точки')
plt.plot(line_X, model.predict(line_X.reshape(-1, 1)), color='red', label='Регрессия')
plt.title("Регрессия на линейном кластере")


plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(script_dir / f'Регрессия на линейном кластере.png')
plt.close()

print("Оценка линейной регрессии:")
print(f"  MSE  = {mse:.4f}")
print(f"  RMSE = {rmse:.4f}")
print(f"  MAE  = {mae:.4f}")
print(f"  R²   = {r2:.4f}")

#Оценка линейной регрессии:
#  MSE  = 0.0334
#  RMSE = 0.1828
#  MAE  = 0.1425
#  R²   = 0.9949
#>>>