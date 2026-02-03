import requests
import json
import os

DATABRICKS_SQL_ENDPOINT = os.getenv("DATABRICKS_SQL_ENDPOINT")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")


def write_event(event: dict) -> None:
    payload = {
        "statment": f"""
        INSERT INTO manufacturing.bronze.equipments_events VALUES (
            '{event["event_id"]}',
            '{event["equipament_id"]}',
            '{event["sensor_type"]}',
            '{event["sensor_value"]}',
            '{event["unit"]}',
            TIMESTAMP '{event["event_timestamp"].isoformat()}',
            current_timestamp()
        )
        """
    }

    headers = {
        "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    }

    requests.post(DATABRICKS_SQL_ENDPOINT, json=payload, headers=headers)
