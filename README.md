# Homework: Data & ML Orchestration with Apache Airflow

Goal: Airflow UI, existing pipelines, AI-assisted DAG development.

## 1. Manual execution (70 points)

- Deployed Airflow + MLflow with Docker Compose. UIs: Airflow `:8080`, MLflow `:5000`.
- Unpaused and triggered `telco_churn_training_pipeline`.
- HITL: approved `approve_promotion` in Required Actions.
- Assets: `telco_churn_champion_model` automatically triggered `telco_churn_batch_scoring`.

Screenshots: [`screenshots/`](screenshots/)

| File | Content |
|---|---|
| [01-airflow-home.png](screenshots/01-airflow-home.png) | Home: successful DAG runs, asset events → scoring |
| [02-dags.png](screenshots/02-dags.png) | DAGs unpaused, last runs success |
| [03-training-pipeline.png](screenshots/03-training-pipeline.png) | Training graph green, HITL done, asset events |
| [04-assets.png](screenshots/04-assets.png) | `telco_churn_champion_model` |
| [05-mlflow.png](screenshots/05-mlflow.png) | MLflow experiment `telco-churn-airflow` |
| [06-mlflow-experiment.png](screenshots/06-mlflow-experiment.png) | Model registry: `TelcoChurnModel` v3 alias `champion` |

## 2. Prompt engineering (30 points)

Prompt: [PROMPT.md](PROMPT.md)

Generated DAG (Airflow 3 `airflow.sdk`, TaskFlow, FileSensor, idempotent row count, XCom):  
[`dags/data_csv_row_count.py`](dags/data_csv_row_count.py)

Successful run: `row_count=5` (see DAGs screenshot).

## Agent usage

[AGENT.md](AGENT.md)
