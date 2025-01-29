from fastapi import APIRouter, status
import joblib
from preprocessing.cleaning import apply_min_max
from preprocessing.data_discretization import create_category_time
from preprocessing.feature_engineering import apply_feature_engineering
from preprocessing.final_cleaning import apply_final_cleaning
from schemas import SensorData
from log import get_log
from utils import *
from typing import List
from datetime import datetime
import pandas as pd
import os

log = get_log(__name__)
router = APIRouter()

buffer: List[SensorData] = []
SENSOR_NUMBER = 15
WINDOW_SIZE = 25
# load the model
RF = joblib.load('../classification/RF.pkl')
# initialize the dataframe
df_sensor = pd.read_csv(os.path.join('../dataset','Sensor_Occupancy_Estimation.csv'), index_col=0)

@router.post("/start", status_code=status.HTTP_200_OK)
async def retrieve_parameters():
    # dataframe for input
    df_in = pd.read_csv(os.path.join('../dataset','In_Occupancy_Estimation.csv'), index_col=0)
    log.info("Received data from the master zigbee")
    # simulate data from the master zigbee
    for i in range(SENSOR_NUMBER):
        value = generate_value(df_sensor.columns[i])
        buffer.append(SensorData(timestamp=datetime.now(), node=df_sensor.columns[i], value=value))

    log.info("Values generated")
    unified_timestamp = min(data.timestamp for data in buffer)
    unified_date = unified_timestamp.date()
    log.info(f"Data: {unified_date}")
    unified_time = unified_timestamp.time().strftime('%H:%M:%S')
    df_in.loc[0,"Date"] = unified_date
    df_in.loc[0,"Time"] = unified_time
    log.info(f"Buffer dimension {len(buffer)}")
    for data in buffer:
        df_in.loc[0, data.node] = data.value

    log.info("Cleaning buffer")
    buffer.clear()
    log.info("Apply cleaning and normalization")
    apply_min_max(df_in)
    # retrieve new row
    row_in = df_in.iloc[[0]]
    log.info(f"Row in: {row_in}")
    log.info("Normalization completed")
    # adding to feature engineering dataset
    df_feature_engineering = pd.read_csv(os.path.join('../dataset','Feature_Engineering_Occupancy_Estimation.csv'), index_col=0)
    df_feature_engineering = pd.concat([df_feature_engineering, row_in], ignore_index=True)
    # Check dimension and remove first row
    if len(df_feature_engineering) > WINDOW_SIZE:
        log.info("Removing first row")
        df_feature_engineering = df_feature_engineering.iloc[1:].reset_index(drop=True)
    
    # save the dataframe
    df_feature_engineering.to_csv(os.path.join('../dataset','Feature_Engineering_Occupancy_Estimation.csv'))
    # dataframe with all features
    df_full = pd.read_csv(os.path.join('../dataset','Full_Features_Occupancy_Estimation.csv'), index_col=0)
    df_full = pd.concat([df_full, row_in], ignore_index=True)
    # apply feature engineering
    log.info("Apply feature engineering")
    apply_feature_engineering(df_feature_engineering, df_full)
    # create category time
    log.info("Create time category")
    create_category_time(df_full)
    # apply final cleaning
    log.info("Apply final cleaning")
    apply_final_cleaning(df_full)
    # use model to predict
    log.info("Predicting number people")
    df_final = pd.read_csv(os.path.join('../dataset','Final_Cleaned_Occupancy_Estimation.csv'),index_col=0)
    prediction = RF.predict(df_final)
    log.info(f"Prediction: {prediction}")
    prediction_list = prediction.tolist()
    return {"prediction": prediction_list}
