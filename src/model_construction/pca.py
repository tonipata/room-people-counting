from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from data_discretization import time_discretization

pca = PCA()

df = pd.read_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'),index_col=0)

target_index = df.columns.get_loc('Room_Occupancy_Count')
features : np.ndarray = time_discretization(df.values)
#print(features)
# remove target column
df_pca = pd.DataFrame(features[:,:-1])

X = df_pca
X_pca = pca.fit_transform(X)

# Cumulative Explained Variance
explained_variance_ratio = np.cumsum(pca.explained_variance_ratio_)

# Graph of Cumulative Explained Variance
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o', linestyle='--')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('PCA - Explained Variance')
plt.grid()
plt.show()