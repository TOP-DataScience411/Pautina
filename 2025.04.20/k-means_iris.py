from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from seaborn import pairplot, heatmap
from pandas import DataFrame
from matplotlib import pyplot as plt

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data = load_iris()

x = data.data
y = data.target
feature_names = data.feature_names

plt.figure(figsize = (10, 6))
df = DataFrame(x, columns = data.feature_names)
df['target'] = y
pairplot(df, hue = 'target', palette = 'viridis')
plt.savefig(path_dir / 'iris_pairplot.png', dpi = 200)

k_values = [0.1, 1, 10, 100]
n_clusters = 3
feature_indexes = range(4)

results = []
for idx in feature_indexes:
    for k in k_values:
        x_k = x.copy()
        x_k[:, idx] *= k

        kmeans = KMeans(n_clusters = n_clusters, random_state=1)
        clusters = kmeans.fit_predict(x_k)

        silhouette = silhouette_score(x_k, clusters)
        results.append({
            'feature': feature_names[idx],
            'k': k,
            'silhouette': silhouette
        })

        pca = PCA(n_components = 2)
        X_pca = pca.fit_transform(x_k)

        plt.figure(figsize = (6, 4))
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c = clusters, cmap = 'viridis')
        plt.title(f"{feature_names[idx]} × {k}\nSilhouette: {silhouette:.2f}")
        plt.xlabel("PCA 1"), plt.ylabel("PCA 2")
        plt.savefig(path_dir / f"iris_{feature_names[idx]}_k{k}.png")


results_df = DataFrame(results)
pivot_table = results_df.pivot(index = 'feature', columns= 'k', values = 'silhouette')

plt.figure(figsize = (14, 8))
heatmap(pivot_table, annot = True, cmap = 'PuBuGn')
plt.title('Silhouette Scores')
plt.savefig(path_dir / 'iris_heatmap.png')

print(pivot_table)


#k                     0.1       1.0       10.0      100.0
#feature
#petal length (cm)  0.472932  0.551192  0.669549  0.677733
#petal width (cm)   0.549748  0.551192  0.689637  0.724549
#sepal length (cm)  0.591179  0.551192  0.527939  0.540308
#sepal width (cm)   0.581443  0.551192  0.411646  0.521629
#>>>