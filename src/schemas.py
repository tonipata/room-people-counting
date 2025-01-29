from typing import Union, List
from pydantic import BaseModel
from datetime import datetime

# define the object coming from the master zigbee
class SensorData (BaseModel):
    timestamp: datetime
    node: str
    value: Union[float, int]