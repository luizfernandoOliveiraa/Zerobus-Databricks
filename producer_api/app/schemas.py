from pydantic import BaseModel
from datetime import datetime


class SensorEvent(BaseModel):
    event_id: str
    equipament_id: str
    sensor_type: str
    sensor_value: float
    unit: str
    event_timestamp: datetime
