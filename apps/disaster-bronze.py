from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# ─── Spark Session Config ─────────────────────────────────────────
spark = (
    SparkSession.builder
    .appName("DisasterAlertStreamingLakehouse")
    # cluster master
    .master("spark://spark-master:7077")
    # delta lake
    .config("spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .enableHiveSupport()
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

# ─── Kafka Raw Stream ─────────────────────────────────────────────
raw_stream = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "disaster-alert-topic")
    .option("startingOffsets", "latest")
    .load()
)

# ─── Convert Binary to String ─────────────────────────────────────
json_stream = raw_stream.selectExpr(
    "CAST(value AS STRING) as raw_json",
    "timestamp as kafka_timestamp"
)

# ─── Flexible Schema ──────────────────────────────────────────────
# threat_index is StringType to safely handle dirty events
# where the value may be "LOW", "HIGH", "CRITICAL" instead of an integer
disaster_schema = StructType([
    StructField("sensor_id",     StringType()),
    StructField("station_id",    StringType()),
    StructField("region",        StringType()),
    StructField("threat_index",  StringType()),   # flexible: handles int + string dirty values
    StructField("alert_level",   IntegerType()),
    StructField("disaster_type", StringType()),
    StructField("event_time",    StringType())
])

parsed = json_stream.withColumn(
    "data",
    from_json(col("raw_json"), disaster_schema)
)

flattened = parsed.select(
    "raw_json",
    "kafka_timestamp",
    "data.*"
)

# ─── Bronze Delta Write ───────────────────────────────────────────
bronze_query = (
    flattened.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/opt/spark/warehouse/chk/disaster_bronze")
    .option("path", "/opt/spark/warehouse/disaster_bronze")
    .start()
)

spark.streams.awaitAnyTermination()
