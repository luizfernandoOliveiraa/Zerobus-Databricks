"""
Módulo que define os esquemas de dados para eventos de sensores.

Classes:
    - SensorEvent: Modelo de dados para eventos de sensores.
        Contém os atributos:
            - event_id (str): Identificador único do evento.
            - equipment_id (str): Identificador do equipamento associado ao evento.
            - sensor_type (str): Tipo do sensor que gerou o evento.
            - sensor_value (float): Valor medido pelo sensor.
            - unit (str): Unidade de medida do valor do sensor.
            - event_timestamp (datetime): Data e hora em que o evento ocorreu.


"""

from pydantic import BaseModel
from datetime import datetime


class SensorEvent(BaseModel):
    event_id: str
    equipment_id: str
    sensor_type: str
    sensor_value: float
    unit: str
    event_timestamp: datetime
