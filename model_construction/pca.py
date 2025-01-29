from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from sklearn.calibration import LabelEncoder

# Applica il PCA
pca = PCA()
df = pd.read_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'),index_col=0)

# Prepara i dati
encoder = LabelEncoder()
df['Time_Category'] = encoder.fit_transform(df['Time_Category'])
cols = list(df.columns)
cols.remove("Room_Occupancy_Count")
cols.remove("Date")
cols.remove("Time")

X = df[cols]
print(X.columns)
X_pca = pca.fit_transform(X)

# Varianza spiegata cumulativa
explained_variance_ratio = np.cumsum(pca.explained_variance_ratio_)

# Grafico della varianza spiegata cumulativa
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, marker='o', linestyle='--')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('PCA - Explained Variance')
plt.grid()
plt.show()

n_components = 10
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)

# Matrice dei pesi delle feature
loading_matrix = pd.DataFrame(
    np.abs(pca.components_).T,
    columns=[f'PC{i+1}' for i in range(n_components)],
    index=X.columns
)

feature_max_impact = loading_matrix.max(axis=1)
top_10_features_max = feature_max_impact.sort_values(ascending=False).head(10)
print("Top 10 Features con massimo impatto su almeno una componente principale:")
print(top_10_features_max)

ordered_columns = ['Time_Category', 'S1_Light', 'S2_Light', 'S4_Light', 'S1_Sound', 'S2_Sound', 'S3_Sound', 'S5_CO2', 'S6_PIR', 'S7_PIR']
df_reduced = df[ordered_columns + ["Room_Occupancy_Count"]]
# save the reduced dataset
df_reduced.to_csv(os.path.join('../dataset','Reduced_Occupancy_Estimation.csv'))