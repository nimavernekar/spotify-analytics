from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, round

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SpotifyETL") \
    .getOrCreate()

# Read raw JSON file
df_raw = spark.read.json("data/raw/top50_2025-06-25.json")

# Basic transformations
df_transformed = df_raw.withColumn("release_date", to_date("release_date")) \
    .withColumn("duration_minutes", round(col("duration_ms") / 60000, 2)) \
    .drop("duration_ms") \
    .select("track_name", "artist", "album", "release_date", "explicit", "popularity", "duration_minutes", "date_fetched")

# Save cleaned data
df_transformed.write.mode("overwrite").parquet("output/curated/spotify_daily_top.parquet")

print("✅ ETL pipeline completed. Curated data saved to output/curated/")
