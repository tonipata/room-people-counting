import os
import pandas as pd

def apply_min_max(df: pd.DataFrame):
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