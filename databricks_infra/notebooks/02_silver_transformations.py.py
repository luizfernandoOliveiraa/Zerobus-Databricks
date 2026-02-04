# Databricks notebook source
# MAGIC %sql 
# MAGIC
# MAGIC SET CATALOG manufacturing

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS manufacturing.silver

# COMMAND ----------

# MAGIC %md
# MAGIC ### Criando a tablema Silver, realizando somente ajustes pequenos nos dados, e realizando full load, mais uma vez aqui a intenção é aplicar os conceitos do zerobus/zero copy, por isso a escolha entre o tipo de insert dos dados nao foi uma prioridade.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE manufacturing.silver.equipment_events_clean AS 
# MAGIC SELECT
# MAGIC   equipment_id,
# MAGIC   sensor_type,
# MAGIC   sensor_value,
# MAGIC   unit,
# MAGIC   event_timestamp
# MAGIC FROM manufacturing.bronze.equipments_events
# MAGIC WHERE sensor_value IS NOT NULL
