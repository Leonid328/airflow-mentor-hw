# Prompt used for the DAG

```
You are an Airflow 3 DAG author. Generate a complete, production-minded DAG file.

Constraints:
- Airflow 3 only. Import from airflow.sdk (dag, task, get_current_context). Do NOT use airflow.decorators, airflow.models.DAG, or airflow.datasets.
- Use the TaskFlow API (@dag / @task) for Python work.
- Sensors and file waiting: use apache-airflow-providers-standard (e.g. FileSensor or @task.sensor / PokeReturnValue) — not airflow.sensors.filesystem from 2.x.
- Best practices:
  - Task idempotency: counting rows must be a pure function of the current file contents; re-running the task must not append, mutate, or delete data.csv; no timestamps as unique keys; mkdir exist_ok=True if needed.
  - Keep DAG parsing light: import pandas/csv only inside task bodies.
  - XCom only for small metadata (an integer row count), never the file body.
  - catchup=False, retries on the count task, owner set, timezone-aware start_date (pendulum).
  - Do not use Variable/Connection unless required.

Behavior:
1. Sensor task: wait until /data/data.csv exists (poke_interval ~30s, timeout reasonable, mode poke). Path is exactly /data/data.csv.
2. Downstream TaskFlow task: open that file, count data rows (exclude header if present), return the integer count.
3. Downstream TaskFlow task: receive the count via XCom (TaskFlow argument passing, not xcom_pull templates) and print it to logs (print or logging).

Output: a single Python module ready to drop into dags/, with docstring, no extra commentary outside the file.
```
