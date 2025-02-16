import pandas as pd
import os
import numpy as np

def time_discretization(features: np.ndarray) -> np.ndarray:
    df_original = pd.read_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'),index_col=0)
    time_index = df_original.columns.get_loc('Time')
    data_index = df_original.columns.get_loc('Date')
    df = pd.DataFrame(features)
    time_bin = pd.to_datetime(df.iloc[:, time_index], format='%H:%M:%S').dt.hour.between(9, 19).astype(int)
    df.iloc[:, time_index] = time_bin
    df = df.drop(df.columns[data_index], axis=1)
    return df.values