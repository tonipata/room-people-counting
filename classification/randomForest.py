from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,f1_score, make_scorer, precision_score, recall_score
import pandas as pd
import os
from sklearn.model_selection import StratifiedKFold
import joblib
from sklearn.calibration import LabelEncoder

# Carica il dataset
df = pd.read_csv(os.path.join('../dataset','Reduced_Occupancy_Estimation.csv'),index_col=0)

# # Prepara i dati
# encoder = LabelEncoder()
# df['Time_Category'] = encoder.fit_transform(df['Time_Category'])
# Prepara i dati
cols = list(df.columns)
cols.remove("Room_Occupancy_Count")
# cols.remove("Date")
# cols.remove("Time")
X = df[cols]
y = df['Room_Occupancy_Count']

# Dividi il dataset in training e testing in modo stratificato
skf = StratifiedKFold(n_splits=10, random_state=42, shuffle=True)

# Inizializza e allena il modello RF
model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_split=2, min_samples_leaf=1, criterion='gini', random_state=42)

# scoring = {
#     'precision_macro': make_scorer(precision_score, average='macro'),
#     'recall_macro': make_scorer(recall_score, average='macro'),
#     'f1_macro': make_scorer(f1_score, average='macro')
# }

# results = cross_validate(model, X, y, scoring=scoring, cv=skf)

# print ("Risultati della cross-validation:")
# print(f"Average Precision: {results['test_precision_macro'].mean()}")
# print(f"Average Recall: {results['test_recall_macro'].mean()}")
# print(f"Average F1-Score: {results['test_f1_macro'].mean()}")

# split in training e testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
print("Performance finale sui dati di training:")
print(classification_report(y_train, y_train_pred))
y_test_pred = model.predict(X_test)
print("\nPerformance finale sui dati di test:")
print(classification_report(y_test, y_test_pred))

# Salva il modello
joblib.dump(model, 'RF.pkl')