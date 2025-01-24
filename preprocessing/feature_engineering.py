import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

WINDOW_SIZE = 25

# Load the data
df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation_discretization.csv'),index_col=0)
# add new column
df['CO2_Slope'] = np.nan

# Sort the data
df.sort_values(by=['Date','Time'])

# create group based on date
grouped = df.groupby('Date')
# for each group of date compute slope
for group in grouped:
    current_group = group[1]
    for i in range(0, len(current_group)):
        # check if we have enough data points
        if i < WINDOW_SIZE:
            # set 0 as slope
            df.loc[current_group.index[i], 'CO2_Slope'] = 0
            continue

        y = current_group['S5_CO2'].iloc[i-WINDOW_SIZE:i].values

        x = np.arange(WINDOW_SIZE).reshape(-1,1)

        # Linear regression
        reg = LinearRegression().fit(x, y)
        slope = reg.coef_[0]
        df.loc[current_group.index[i], 'CO2_Slope'] = slope

# Move 'CO2_Slope' next to 'S5_CO2'
cols = list(df.columns)
s5_co2_index = cols.index('S5_CO2')
cols.insert(s5_co2_index + 1, cols.pop(cols.index('CO2_Slope')))
df = df[cols]

# # Save the data 
df.to_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'))