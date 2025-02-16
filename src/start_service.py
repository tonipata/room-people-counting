from fastapi import APIRouter, status
import joblib
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
RF = joblib.load('classification/RF_pipeline.pkl')
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
    
    log.info("Predicting number people")
    prediction = RF.predict(df_in)
    log.info(f"Prediction: {prediction}")
    prediction_list = prediction.tolist()
    return {"prediction": prediction_list}
