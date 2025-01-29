import numpy as np
import pandas as pd
import os

WORK = "WORK"
SLEEP = "SLEEP"

def time_to_category(time):
    if 9 <= time.hour < 19:
        return WORK
    else:
        return SLEEP

def create_category_time():
    df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation_Normalized.csv'),index_col=0)
    # create new column 'Time_Category' from 'Time'
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    # Applica la funzione alla colonna 'Time'
    df['Time_Category'] = df['Time'].apply(time_to_category)
    # move 'Time_Category' next to 'Time'
    cols = list(df.columns)
    time_index = cols.index('Time')
    cols.insert(time_index + 1, cols.pop(cols.index('Time_Category')))
    df = df[cols]
    # salva il dataset
    df.to_csv(os.path.join('../dataset','Occupancy_Estimation_Discretization.csv'))

create_category_time()