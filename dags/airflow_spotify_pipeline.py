# dags/airflow_spotify_pipeline.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'nimisha',
    'start_date': datetime(2025, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email': ['your-email@example.com'],
    'email_on_failure': True,
}


with DAG(
    dag_id='spotify_daily_top50_etl',
    default_args=default_args,
    description='Daily Spotify Top 50 Ingestion + ETL Pipeline',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['spotify', 'etl', 'spark'],
) as dag:

    ingest_task = BashOperator(
        task_id='ingest_spotify_data',
        bash_command='source ~/spotify-analytics/venv/bin/activate && python3 ~/spotify-analytics/src/ingestion/spotify_api_ingestion.py'
    )

    transform_task = BashOperator(
        task_id='run_spark_etl',
        bash_command='spark-submit ~/spotify-analytics/src/transformations/spark_etl.py'
    )

    validate_task = BashOperator(
    task_id='validate_data',
    bash_command='source ../venv/bin/activate && python3 src/monitoring/validate_data.py'
    )

    ingest_task >> transform_task >> validate_task
