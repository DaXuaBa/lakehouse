from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("ParquetToCSV").getOrCreate()

# Path to the directory containing Parquet data
parquet_path = "hdfs://localhost:9000/Lakehouse/Silver"

# Read data from all partitions
df = spark.read.option("basePath", parquet_path).parquet(parquet_path)

# Write data to CSV file
csv_output_path = "/home/bach/output"  # Adjust the path accordingly
df.coalesce(1).write.csv(csv_output_path, header=True, mode="overwrite")

# Stop SparkSession
spark.stop()

