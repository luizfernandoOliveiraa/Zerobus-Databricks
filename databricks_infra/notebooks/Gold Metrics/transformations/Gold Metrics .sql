CREATE OR REFRESH STREAMING TABLE hourly_metrics
AS SELECT
  equipment_id,
  sensor_type,
  window(event_timestamp, '1 hour') AS hour_window,
  avg(sensor_value) as avg_value,
  max(sensor_value) as max_value
FROM STREAM manufacturing.silver.equipment_events_clean
GROUP BY equipment_id, sensor_type, hour_window