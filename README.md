# Disaster Alert System

## Overview
The Disaster Alert & Monitoring System is a real-time data engineering project developed to stream, process, and analyze disaster threat signals from sensor networks deployed across disaster-prone regions. It integrates data related to sensor readings, monitoring stations, geographic regions, and alert levels to understand disaster patterns and enable rapid response.

The project utilizes the Medallion Architecture to process data through Bronze, Silver, and Gold layers, revealing critical patterns in disaster activity to support emergency response planning.


<p align="center">
<img src="https://img.shields.io/badge/Apache_Kafka-000000?style=for-the-badge&logo=apachekafka&logoColor=white">
<img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
<img src="https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=databricks&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
</p>

Apache Kafka: Real-time event streaming backbone
Apache Spark: Structured Streaming for multi-layer data processing
Delta Lake: Reliable lakehouse storage with ACID transactions
Hive Metastore: Centralized metadata and schema management
Power BI: Interactive dashboards for real-time monitoring.

## Real-Time Data Simulation

Before ingestion, a Python-based producer simulates a network of sensors streaming a mix of 70% clean and 30% dirty data to mimic real-world challenges.





### Simulation Highlights
-Geographic Regions: Coastal, Hillside, Forest, Urban, Riverbank, Desert
-Disaster Types: Earthquake, Flood, Wildfire, Tsunami, Landslide, Cyclone,Volcano.
-Dirty Data Injection: Includes null values, negative indices, duplicates, and corrupt JSON to test pipeline resilience.






