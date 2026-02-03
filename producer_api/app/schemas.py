from pydantic import BaseModel
from datetime import datetime


class SensorEvent(BaseModel):
    event_id: int
    equipment_id: str
    sensor_type: str
    sensor_value: float
    unit: int
    event_timestamp: datetime
