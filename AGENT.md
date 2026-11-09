# Agent usage

## Error analysis

Scenario: `select_best` fails because F1 is below 0.99. Recovery **without editing DAG code**.

The quality gate is the DAG param `min_metric_threshold` (workshop demo fail uses `0.99`). Real F1 on this telco set is far below 0.99, so `select_best` raises `ValueError` on purpose.

1. Trigger a **new** run with `min_metric_threshold=0.5` (or another reachable value).
2. Do **not** Clear `select_best` on the same run that still has `0.99` — it will fail again.
3. No need to retrain mapped `train_model` tasks if you only change the param and start a new DAG run.

## Optimization

Airflow UI keeps restarting: give Docker **at least 4 GB RAM, ideally 8 GB** (assignment README §5 / §10). OOM on the API server causes 502 and `restart: unless-stopped` loops. Do not inject `_PIP_ADDITIONAL_REQUIREMENTS` on every boot; ML libs are already in the image. Confirm MLflow healthcheck is green before expecting Airflow to stay up.
