# 🎵 Spotify Analytics Pipeline

An end-to-end data engineering project that ingests Spotify Top 50 data daily using the Spotify API, processes it using PySpark, and orchestrates the pipeline with Apache Airflow. Built to demonstrate scalable, modular, and production-style pipelines.

## 🚀 Tech Stack

- Python
- Spotify Web API via `Spotipy`
- PySpark
- Apache Airflow
- Parquet Files
- Jupyter Notebooks / Power BI
- GitHub

## 📊 What This Project Does

- 🔄 Fetches Spotify Top 50 Daily Chart via API
- 🧹 Cleans and transforms the data using PySpark
- 🗂️ Writes curated parquet datasets to `/output`
- ⏱️ Runs automated daily jobs using Airflow
- 📈 Enables dashboarding with Jupyter or Power BI

## 📂 Project Structure
``` bash
spotify-analytics/
├── data/ # Raw & processed data
├── dags/ # Airflow DAGs
├── src/
│ ├── ingestion/ # Spotify API ingestion
│ └── transformations/ # PySpark batch ETL
├── notebooks/ # Visual exploration
├── output/ # Final curated files
├── .env # Credentials (excluded in GitHub)
├── requirements.txt
├── README.md

```

## 📌 How to Run


1. Create virtualenv and install
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Set up Spotify API credentials in a .env file
```bash
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

3. Ingest data
```bash
python src/ingestion/spotify_api_ingestion.py
```

4. Run ETL
```bash
python src/transformations/spark_etl.py
```

5. Launch Airflow
```bash
airflow standalone
```
