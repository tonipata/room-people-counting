import numpy as np
import pandas as pd
import os
from sklearn.calibration import LabelEncoder

def apply_final_cleaning(df: pd.DataFrame):
    # drop 2 features
    cols = list(df.columns)
    time_index = cols.index('Time')
    cols.insert(time_index + 1, cols.pop(cols.index('Time_Category')))
    df = df[cols].copy()
    drop_cols = ['Date','Time', 'S1_Temp', 'S2_Temp', 'S3_Temp', 'S4_Temp', 'S3_Light', 'S4_Sound', 'S5_CO2_Slope']
    df.drop(columns=drop_cols, inplace=True)
    # encoder
    encoder = LabelEncoder()
    df['Time_Category'] = encoder.fit_transform(df['Time_Category'])
    # save the dataframe
    df.to_csv(os.path.join('../dataset', 'Final_Cleaned_Occupancy_Estimation.csv'), index=True)