from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Read Large JSONL Files") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

# Read JSONL files
file_path = "/path/to/data"
df = spark.read.json(file_path)

# Print schema and show sample rows
df.printSchema()
df.show(5)

# Save the DataFrame to Parquet
df.write.mode("overwrite").parquet("/path/to/output")

# Stop Spark session
spark.stop()
