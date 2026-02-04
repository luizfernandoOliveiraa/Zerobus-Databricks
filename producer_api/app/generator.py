"""
Módulo responsável por gerar eventos de sensores de equipamentos.

Classes:
    - SensorEvent: Modelo de dados para eventos de sensores.
    Contém os atributos:
        - event_id (str): Identificador único do evento.
        - equipment_id (str): Identificador do equipamento associado ao evento.
        - sensor_type (str): Tipo do sensor que gerou o evento.
        - sensor_value (float): Valor medido pelo sensor.
        - unit (str): Unidade de medida do valor do sensor.
        - event_timestamp (datetime): Data e hora em que o evento ocorreu.
Functions:
    - generate_event() -> SensorEvent:
        Gera um evento fictício de sensor com dados aleatórios.

"""

import uuid
import random
from faker import Faker
from datetime import datetime
from .schemas import SensorEvent

fake = Faker()

SENSORS = {
    "temperature": ("°C", 1000, 1800),
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
