"""
Módulo responsável por escrever eventos de sensores no Databricks.

Functions:
    - write_event(event: dict):
        Escreve um evento de sensor no Databricks usando o conector SQL.
        O evento deve ser passado como um dicionário com as chaves:
            - event_id (str): Identificador único do evento.
            - equipment_id (str): Identificador do equipamento associado ao evento.
            - sensor_type (str): Tipo do sensor que gerou o evento.
            - sensor_value (float): Valor medido pelo sensor.
            - unit (str): Unidade de medida do valor do sensor.
            - event_timestamp (datetime): Data e hora em que o evento ocorreu.

"""

import os
import dotenv
from databricks import sql

dotenv.load_dotenv()

DATABRICKS_SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")


def write_event(event: dict):
    query = f"""
        INSERT INTO manufacturing.bronze.equipments_events VALUES (
            '{event["event_id"]}',
            '{event["equipment_id"]}',
            '{event["sensor_type"]}',
            '{event["sensor_value"]}',
            '{event["unit"]}',
            '{event["event_timestamp"]}',
            current_timestamp()
        )
    """
    try:
        with sql.connect(
            server_hostname=DATABRICKS_SERVER_HOSTNAME,
            http_path=DATABRICKS_HTTP_PATH,
            access_token=DATABRICKS_TOKEN,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
        print(f"Event written successfully: {event['event_id']}")
    except Exception as e:
        print(f"Failed to write event: {e}")
