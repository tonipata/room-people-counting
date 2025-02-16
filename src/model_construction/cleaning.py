import pandas as pd
import os

# remove 'S5_CO2_Slope' column
df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation.csv'),index_col=0)
df.drop('S5_CO2_Slope', axis=1, inplace=True)
df.reset_index(inplace=True)
# drop rows with null values
df.dropna(inplace=True)
# save
df.to_csv(os.path.join('../dataset','New_Occupancy_Estimation.csv'))