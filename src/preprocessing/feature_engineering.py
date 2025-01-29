import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

WINDOW_SIZE = 25

def apply_feature_engineering(df_feature_engineering: pd.DataFrame, df_full: pd.DataFrame):
    num_rows = len(df_feature_engineering)

    # check if we have enough data points
    if num_rows < WINDOW_SIZE:
        # set 0 as slope
        df_full.loc[0,'S5_CO2_Slope'] = 0
    else:
        y = df_feature_engineering['S5_CO2'].values
        x = np.arange(WINDOW_SIZE).reshape(-1,1)

        # Linear regression
        reg = LinearRegression().fit(x, y)
        slope = reg.coef_[0]
        df_full.loc[0, 'S5_CO2_Slope'] = slope