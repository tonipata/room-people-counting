import pandas as pd
import os

WORK = "WORK"
SLEEP = "SLEEP"

def time_to_category(time):
    if 9 <= time.hour < 19:
        return WORK
    else:
        return SLEEP

def create_category_time(df: pd.DataFrame):
    # create new column 'Time_Category' from 'Time'
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    # Applica la funzione alla colonna 'Time'
    df['Time_Category'] = df['Time'].apply(time_to_category)