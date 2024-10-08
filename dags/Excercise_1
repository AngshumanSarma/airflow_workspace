from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

procure_rocket_material >> [build_stage_1, build_stage_2, build_stage_3]
procure_fuel >> build_stage_3
[build_stage_1, build_stage_2, build_stage_3] >> launch
