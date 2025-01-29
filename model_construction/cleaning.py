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
def save_min_max():
    # create a dataframe
    df_normalization = pd.DataFrame()
    # take min of dataset
    df_normalization['Min_Temp1'] = [df['S1_Temp'].min()]
    df_normalization['Min_Temp2'] = [df['S2_Temp'].min()]
    df_normalization['Min_Temp3'] = [df['S3_Temp'].min()]
    df_normalization['Min_Temp4'] = [df['S4_Temp'].min()]
    df_normalization['Min_Light1'] = [df['S1_Light'].min()]
    df_normalization['Min_Light2'] = [df['S2_Light'].min()]
    df_normalization['Min_Light3'] = [df['S3_Light'].min()]
    df_normalization['Min_Light4'] = [df['S4_Light'].min()]
    df_normalization['Min_Sound1'] = [df['S1_Sound'].min()]
    df_normalization['Min_Sound2'] = [df['S2_Sound'].min()]
    df_normalization['Min_Sound3'] = [df['S3_Sound'].min()]
    df_normalization['Min_Sound4'] = [df['S4_Sound'].min()]
    df_normalization['Min_CO2'] = [df['S5_CO2'].min()]
    # take max of dataset
    df_normalization['Max_Temp1'] = [df['S1_Temp'].max()]
    df_normalization['Max_Temp2'] = [df['S2_Temp'].max()]
    df_normalization['Max_Temp3'] = [df['S3_Temp'].max()]
    df_normalization['Max_Temp4'] = [df['S4_Temp'].max()]
    df_normalization['Max_Light1'] = [df['S1_Light'].max()]
    df_normalization['Max_Light2'] = [df['S2_Light'].max()]
    df_normalization['Max_Light3'] = [df['S3_Light'].max()]
    df_normalization['Max_Light4'] = [df['S4_Light'].max()]
    df_normalization['Max_Sound1'] = [df['S1_Sound'].max()]
    df_normalization['Max_Sound2'] = [df['S2_Sound'].max()]
    df_normalization['Max_Sound3'] = [df['S3_Sound'].max()]
    df_normalization['Max_Sound4'] = [df['S4_Sound'].max()]
    df_normalization['Max_CO2'] = [df['S5_CO2'].max()]
    # save this value
    df_normalization.to_csv('../dataset/Min_Max_Value.csv')


# apply min max normalization
def apply_min_max():
    # retrieve value from file
    df_min_max = pd.read_csv(os.path.join('../dataset','Min_Max_Value.csv'), index_col=0)

    df['S1_Temp'] = (df['S1_Temp'] - df_min_max['Min_Temp1'].iloc[0]) / (df_min_max['Max_Temp1'].iloc[0] - df_min_max['Min_Temp1'].iloc[0])
    df['S2_Temp'] = (df['S2_Temp'] - df_min_max['Min_Temp2'].iloc[0]) / (df_min_max['Max_Temp2'].iloc[0] - df_min_max['Min_Temp2'].iloc[0])
    df['S3_Temp'] = (df['S3_Temp'] - df_min_max['Min_Temp3'].iloc[0]) / (df_min_max['Max_Temp3'].iloc[0] - df_min_max['Min_Temp3'].iloc[0])
    df['S4_Temp'] = (df['S4_Temp'] - df_min_max['Min_Temp4'].iloc[0]) / (df_min_max['Max_Temp4'].iloc[0] - df_min_max['Min_Temp4'].iloc[0])
    df['S1_Light'] = (df['S1_Light'] - df_min_max['Min_Light1'].iloc[0]) / (df_min_max['Max_Light1'].iloc[0] - df_min_max['Min_Light1'].iloc[0])
    df['S2_Light'] = (df['S2_Light'] - df_min_max['Min_Light2'].iloc[0]) / (df_min_max['Max_Light2'].iloc[0] - df_min_max['Min_Light2'].iloc[0])
    df['S3_Light'] = (df['S3_Light'] - df_min_max['Min_Light3'].iloc[0]) / (df_min_max['Max_Light3'].iloc[0] - df_min_max['Min_Light3'].iloc[0])
    df['S4_Light'] = (df['S4_Light'] - df_min_max['Min_Light4'].iloc[0]) / (df_min_max['Max_Light4'].iloc[0] - df_min_max['Min_Light4'].iloc[0])
    df['S1_Sound'] = (df['S1_Sound'] - df_min_max['Min_Sound1'].iloc[0]) / (df_min_max['Max_Sound1'].iloc[0] - df_min_max['Min_Sound1'].iloc[0])
    df['S2_Sound'] = (df['S2_Sound'] - df_min_max['Min_Sound2'].iloc[0]) / (df_min_max['Max_Sound2'].iloc[0] - df_min_max['Min_Sound2'].iloc[0])
    df['S3_Sound'] = (df['S3_Sound'] - df_min_max['Min_Sound3'].iloc[0]) / (df_min_max['Max_Sound3'].iloc[0] - df_min_max['Min_Sound3'].iloc[0])
    df['S4_Sound'] = (df['S4_Sound'] - df_min_max['Min_Sound4'].iloc[0]) / (df_min_max['Max_Sound4'].iloc[0] - df_min_max['Min_Sound4'].iloc[0])
    df['S5_CO2'] = (df['S5_CO2'] - df_min_max['Min_CO2'].iloc[0]) / (df_min_max['Max_CO2'].iloc[0] - df_min_max['Min_CO2'].iloc[0])

    # save the normalized dataset
    df.to_csv('../dataset/Occupancy_Estimation_Normalized.csv')

save_min_max()
apply_min_max()