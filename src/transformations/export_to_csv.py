from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ParquetToCSV") \
    .getOrCreate()

# Load the curated parquet file
df = spark.read.parquet("output/curated/spotify_daily_top.parquet")

# Export as CSV
df.write.option("header", True).mode("overwrite").csv("output/export/spotify_top50_csv")

print("✅ Export complete: CSV files saved to output/export/spotify_top50_csv/")
spark.stop()
