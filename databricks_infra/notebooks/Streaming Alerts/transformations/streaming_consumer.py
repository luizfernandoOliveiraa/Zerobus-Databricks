import dlt
from pyspark.sql.functions import window, avg

@dlt.table(
  name="temperature_alerts_dlt",
  comment="Average temperature alerts per 5-minute window"
)
def temperature_alerts():
    df = (
        dlt.read_stream("manufacturing.bronze.equipments_events")
        .withWatermark("event_timestamp", "10 minutes")
    )

    return (
        df
        .groupBy(
            window("event_timestamp", "5 minutes"),
            "equipment_id"
        )
        .agg(avg("sensor_value").alias("avg_temp"))
        .filter("avg_temp > 1400")
    )
