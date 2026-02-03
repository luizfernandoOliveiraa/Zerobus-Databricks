import uuid
import random
from faker import Faker
from datetime import datetime
from .schemas import SensorEvent

fake = Faker()

SENSORS = {
    "temperature": ("°C", 1000, 1500),
    "pressure": ("bar", 20, 40),
    "vibration": ("mm/s", 0, 10),
}


def generate_event() -> SensorEvent:
    sensor_type = random.choice(list(SENSORS.keys()))
    unit, min_v, max_v = SENSORS[sensor_type]

    return SensorEvent(
        event_id=str(uuid.uuid4()),
        equipment_id=f"F{random.randint(1, 100)}",
        sensor_type=sensor_type,
        sensor_value=round(random.uniform(min_v, max_v), 2),
        unit=unit,
        event_timestamp=datetime.now(),
    )
