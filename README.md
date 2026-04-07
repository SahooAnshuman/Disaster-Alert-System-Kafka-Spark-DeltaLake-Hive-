# Disaster Monitoring Analysis [Kafka + Apache Spark + DeltaLake + Hive Metastore + Power BI]

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
<img width="956" height="649" alt="image" src="https://github.com/user-attachments/assets/4dcaae63-336c-4f1d-9d2b-cb4b7543322a" />

Apache Kafka : Real-time event streaming backbone
Apache Spark : Structured Streaming for multi-layer data processing
Delta Lake : Reliable lakehouse storage with ACID transactions
Hive Metastore : Centralized metadata and schema management
Power BI : Interactive dashboards for real-time monitoring.

## Real-Time Data Simulation

Before ingestion, a Python-based producer simulates a network of sensors streaming a mix of 70% clean and 30% dirty data to mimic real-world challenges.


### Dataset Highlights
- Geographic Regions : Coastal, Hillside, Forest, Urban, Riverbank, Desert  
- Disaster Types : Earthquake, Flood, Wildfire, Tsunami, Landslide, Cyclone,Volcano.
- Dirty Data Injection : Includes null values, negative indices, duplicates, and corrupt JSON to test pipeline resilience.


## Data Pipeline (Medallion Architecture)
The pipeline refines raw sensor data into actionable business intelligence across three distinct layers :
### Bronze Layer (Raw Ingestion)

- Ingests raw Kafka streams into Delta Lake 
-  Preserves full original schema and raw JSON for auditability.

 ### Silver Layer (Quality & Enrichment)
 - Applies data quality checks and deduplication.
 - Feature Engineering: Creates threat_band (Low to Catastrophic), critical_flag for emergency triggers, and night_flag for time-sensitive response.
 ### Gold Layer (Dimensional Modeling)
 - Produces optimized Star Schema tables: fact_disaster, dim_region, and dim_station
 - Structured for high-performance analytical querying
 ## Business Intelligence & SQL Analysis
 Dedicated SQL views are created to bridge the gap between the storage layer and visualization tools.
 ### SQL View Collection
 - bi_fact_disaster : Enriched fact data with explicit type casting for Power BI.
 - bi_dim_region : Mapping of regional risk levels and geographic types.
 - bi_dim_station : Detailed monitoring station metadata and response times.



The system supports real-time monitoring via the Apache Spark Thrift Server using DirectQuery mode for live insights.

### Power BI Desktop
<img width="1917" height="1018" alt="Screenshot 2026-04-07 211215" src="https://github.com/user-attachments/assets/209976a0-ea38-475b-9ee3-7a6a720a5ef7" />
## Power BI Monitoring Dashboard
<img width="1173" height="658" alt="image" src="https://github.com/user-attachments/assets/12aa85dc-6b24-4d7b-b7c9-be0026d302ee" />

### Tooltip [region_type]
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/e512acec-38ed-4cd0-ad6e-769b03467e24" />

linking with the page :
<img width="1272" height="713" alt="image" src="https://github.com/user-attachments/assets/39220e37-9c2d-4126-b7d5-a991cf680de4" />

### Dashboard Insights
- Global Monitoring : KPI cards for threat indices, alert levels, and critical flags.
- Station Performance : Comparison of response times and event contributions by station type.
- Drill-Down Analytics : Custom tooltips linked to treemaps for region-specific disaster severity.

## Project Summary
This project demonstrates an end-to-end real-time data engineering lifecycle. By combining Kafka for ingestion, Spark & Delta Lake for robust processing, and Power BI for visualization, the system transforms chaotic sensor streams into a reliable disaster monitoring platform.

<p align="center">
Thank you for reviewing this project. I hope these disaster monitoring insights are valuable, informative and useful.</p>

<p align="center">
  🌟⭐⭐⭐🌟
</p>
<h3 align="center">Expression of Gratitude</h3>

<p align="center">
  Thank you for reviewing this project. I hope the disaster monitoring insights and the architectural approach presented are informative and useful for your objectives.
</p>

