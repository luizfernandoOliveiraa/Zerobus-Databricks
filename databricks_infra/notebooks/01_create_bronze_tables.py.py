# Databricks notebook source
# MAGIC %md
# MAGIC ## Criação do catálogo de manufacturing e schema bronze dentro no UC.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE CATALOG IF NOT EXISTS manufacturing;
# MAGIC CREATE SCHEMA IF NOT EXISTS manufacturing.bronze;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Criação da tabela bronze, todo esse notebook deve ser rodado apenas 1 vez para criar toda infra do projeto no UC.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Exemplo meramente didático, para prática do conceito e aplicação do zerobus, então a modelagem e definição dos tipos de dados aqui foi meramente para fins de subir a infra o mais rapido possível.

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS manufacturing.bronze.equipments_events (
# MAGIC   event_id STRING,
# MAGIC   equipment_id STRING,
# MAGIC   sensor_type STRING,
# MAGIC   sensor_value FLOAT,
# MAGIC   unit STRING,
# MAGIC   event_timestamp TIMESTAMP,
# MAGIC   ingestion_timestamp TIMESTAMP
# MAGIC )
