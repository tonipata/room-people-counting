import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation.csv'),index_col=0)

# Create a new column for the date
df['Date'] = df.index
# drop index and set it to default
df.reset_index(drop=True, inplace=True)
# insert date as first column
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('Date')))
df = df[cols]
# drop rows with null values
df.dropna(inplace=True)
# drop column with co2 slope
df.drop(columns=['S5_CO2_Slope'], inplace=True)

# normalize the data

# take min of dataset
min_temp1 = df['S1_Temp'].min()
min_temp2 = df['S2_Temp'].min()
min_temp3 = df['S3_Temp'].min()
min_temp4 = df['S4_Temp'].min()
min_light1 = df['S1_Light'].min()
min_light2 = df['S2_Light'].min()
min_light3 = df['S3_Light'].min()
min_light4 = df['S4_Light'].min()
min_CO2 = df['S5_CO2'].min()
# take max of dataset
max_temp1 = df['S1_Temp'].max()
max_temp2 = df['S2_Temp'].max()
max_temp3 = df['S3_Temp'].max()
max_temp4 = df['S4_Temp'].max()
max_light1 = df['S1_Light'].max()
max_light2 = df['S2_Light'].max()
max_light3 = df['S3_Light'].max()
max_light4 = df['S4_Light'].max()
max_CO2 = df['S5_CO2'].max()
# save this value in a file
with open('min_max_values.txt', 'w') as f:
    f.write(f"min_temp1: {min_temp1}\n")
    f.write(f"min_temp2: {min_temp2}\n")
    f.write(f"min_temp3: {min_temp3}\n")
    f.write(f"min_temp4: {min_temp4}\n")
    f.write(f"min_light1: {min_light1}\n")
    f.write(f"min_light2: {min_light2}\n")
    f.write(f"min_light3: {min_light3}\n")
    f.write(f"min_light4: {min_light4}\n")
    f.write(f"min_CO2: {min_CO2}\n")
    f.write(f"max_temp1: {max_temp1}\n")
    f.write(f"max_temp2: {max_temp2}\n")
    f.write(f"max_temp3: {max_temp3}\n")
    f.write(f"max_temp4: {max_temp4}\n")
    f.write(f"max_light1: {max_light1}\n")
    f.write(f"max_light2: {max_light2}\n")
    f.write(f"max_light3: {max_light3}\n")
    f.write(f"max_light4: {max_light4}\n")
    f.write(f"max_CO2: {max_CO2}\n")

# apply min max normalization
df['S1_Temp'] = (df['S1_Temp'] - min_temp1) / (max_temp1 - min_temp1)
df['S2_Temp'] = (df['S2_Temp'] - min_temp2) / (max_temp2 - min_temp2)
df['S3_Temp'] = (df['S3_Temp'] - min_temp3) / (max_temp3 - min_temp3)
df['S4_Temp'] = (df['S4_Temp'] - min_temp4) / (max_temp4 - min_temp4)
df['S1_Light'] = (df['S1_Light'] - min_light1) / (max_light1 - min_light1)
df['S2_Light'] = (df['S2_Light'] - min_light2) / (max_light2 - min_light2)
df['S3_Light'] = (df['S3_Light'] - min_light3) / (max_light3 - min_light3)
df['S4_Light'] = (df['S4_Light'] - min_light4) / (max_light4 - min_light4)
df['S5_CO2'] = (df['S5_CO2'] - min_CO2) / (max_CO2 - min_CO2)

# save the normalized dataset
df.to_csv('../dataset/Occupancy_Estimation_normalized.csv')