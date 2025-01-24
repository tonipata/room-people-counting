from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from datetime import datetime
from typing import Union, List
import os
import pandas as pd

# define the object coming from the master zigbee
class SensorData (BaseModel):
    timestamp: datetime
    node: str
    value: Union[float, int]

df = pd.read_csv(os.path.join('../dataset','Occupancy_Estimation.csv'),index_col=0)
df_temp = pd.DataFrame(columns=df.columns)
# aggiungi una colonna chiamata Date
df_temp['Date'] = df_temp.index
# drop index and set it to default
df_temp.reset_index(drop=True, inplace=True)
# insert date as first column
cols = list(df_temp.columns)
cols.remove("Room_Occupancy_Count")
cols.remove("S5_CO2_Slope")
cols.insert(0, cols.pop(cols.index('Date')))
df_temp = df_temp[cols]

# Prepara i dati
# cols = list(df.columns)
# cols.remove("Room_Occupancy_Count")
# cols.remove("Date")
# cols.remove("Time")

# X = df[cols]
df_temp

# buffer for data from master zigbee
buffer: List[SensorData] = []
SENSOR_NUMBER = 15

# riempi buffer
for i in range(SENSOR_NUMBER):
    buffer.append(SensorData(timestamp=datetime.now(), node=f"node{i}", value=i))

def receive_dat(sensor_data: SensorData):
    if not any(data.node == sensor_data.node for data in buffer):
        buffer.append(sensor_data)
    elif len(buffer) == SENSOR_NUMBER:
        merge_data(buffer)
    else:
        # clear buffer
        buffer.clear()


# def merge_data():
buffer
print(f"BUFFER: {buffer}")
unified_timestamp = min(data.timestamp for data in buffer)
unified_date = unified_timestamp.date()
unified_time = unified_timestamp.time().strftime('%H:%M:%S.%f')[:-4]
print(f"DATA: {unified_date} and TIME: {unified_time}")
# add value data and time to the dataframe
df_temp.loc[0,"Date"] = unified_date
df_temp.loc[0,"Time"] = unified_time
df_temp
# for data in buffer:
#     df_temp.loc[unified_date, data.node] = data.value