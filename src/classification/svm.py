import numpy as np
import pandas as pd
import os
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.metrics import f1_score, make_scorer, precision_score, recall_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, FunctionTransformer
from model_construction.data_discretization import time_discretization
from sklearn.pipeline import Pipeline

df = pd.read_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'),index_col=0)

cols = list(df.columns)
cols.remove("Room_Occupancy_Count")

X = df[cols]
y = df['Room_Occupancy_Count']

time_transformer = FunctionTransformer(time_discretization, validate=False)

model = SVC(kernel='poly', C=1, random_state=42)

estimators = [('time discretization', time_transformer),
               ('scaling',MinMaxScaler()),
               ('pca', PCA(n_components=4)),
               ('rf',model)
            ]

pipeline = Pipeline(estimators)

#tscv = TimeSeriesSplit(n_splits=7)
skf = StratifiedKFold(n_splits=10, random_state=42, shuffle=True)
scoring = {
     'precision_macro': make_scorer(precision_score, average='macro', zero_division=0),
     'recall_macro': make_scorer(recall_score, average='macro', zero_division=0),
     'f1_macro': make_scorer(f1_score, average='macro', zero_division=0)
}
results = cross_validate(pipeline, X, y, scoring=scoring, cv=skf)
 
print ("Risultati della cross-validation:")
print(f"Average Precision: {results['test_precision_macro'].mean()}")
print(f"Average Recall: {results['test_recall_macro'].mean()}")
print(f"Average F1-Score: {results['test_f1_macro'].mean()}")