from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import os
from sklearn.model_selection import StratifiedKFold

# Carica il dataset
df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation_normalized.csv'),index_col=0)

# Prepara i dati
cols = list(df.columns)
cols.remove("Room_Occupancy_Count")
cols.remove("Date")
cols.remove("Time")
X = df[cols]
y = df['Room_Occupancy_Count']

# Dividi il dataset in training e testing in modo stratificato
skf = StratifiedKFold(n_splits=10, random_state=42, shuffle=True)

# Inizializza e allena il modello RF
model = RandomForestClassifier(n_estimators=100, random_state=42)

# cross validation
for fold, (train_index, test_index) in enumerate(skf.split(X, y)):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
#     print(f"Fold {fold+1}")
#     print("\nPerformance sui dati di test:")
#     print(classification_report(y_test, y_test_pred))

# split in training e testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
print("Performance finale sui dati di training:")
print(classification_report(y_train, y_train_pred))
y_test_pred = model.predict(X_test)
print("\nPerformance finale sui dati di test:")
print(classification_report(y_test, y_test_pred))