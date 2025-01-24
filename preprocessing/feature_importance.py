import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, f1_score

df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation.csv'),index_col=0)

X = df.drop(columns=['Room_Occupancy_Count', 'Time', 'S5_CO2_Slope'], axis=1)

y = df['Room_Occupancy_Count']
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
scoring = make_scorer(f1_score, average='macro')

importances = model.feature_importances_ 
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance = feature_importance.sort_values('Importance', ascending=False)

# Build an istogram with the feature importance
plt.figure(figsize=(12, 6))
plt.bar(feature_importance['Feature'], feature_importance['Importance'], color='skyblue')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importances')
plt.xticks(rotation=45)
plt.show()