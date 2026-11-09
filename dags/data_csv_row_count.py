"""Wait for data.csv, count rows, log the count via XCom. Airflow 3 TaskFlow."""

from __future__ import annotations

from datetime import timedelta

import pendulum
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.sdk import dag, task

DATA_CSV = "/opt/airflow/data/data.csv"

DEFAULT_ARGS = {
    "owner": "ml-platform",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


@dag(
    dag_id="data_csv_row_count",
    description="Sensor on data.csv, count rows, print via XCom (homework prompt DAG)",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    default_args=DEFAULT_ARGS,
    tags=["homework", "sensor", "xcom", "taskflow"],
)
def data_csv_row_count():
    wait_for_file = FileSensor(
        task_id="wait_for_data_csv",
        filepath=DATA_CSV,
        poke_interval=10,
        timeout=60 * 30,
        mode="poke",
    )

    @task
    def count_rows() -> int:
        path = DATA_CSV
        with open(path, newline="", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            return 0
        n = len([ln for ln in lines[1:] if ln.strip()])
        print(f"counted {n} data rows in {path}")
        return n

    @task
    def log_count(n: int) -> None:
        print(f"row_count={n}")

    n = count_rows()
    wait_for_file >> n
    log_count(n)


data_csv_row_count()
