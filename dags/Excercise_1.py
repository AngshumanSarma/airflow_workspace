from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="Excercise_1",
    start_date=datetime(year=2019, month=1, day=1),
    end_date=datetime(year=2019, month=1, day=5),
    schedule="@daily",
):
    procure_rocket_material = EmptyOperator(task_id="procure_rocket_material")
    build_stage_1 = EmptyOperator(task_id="build_stage_1")
    build_stage_2 = EmptyOperator(task_id="build_stage_2")
    build_stage_3 = EmptyOperator(task_id="build_stage_3")
    procure_fuel = EmptyOperator(task_id="procure_fuel")
    launch = EmptyOperator(task_id="launch") 


    procure_rocket_material >> [build_stage_1, build_stage_2, build_stage_3]
    procure_fuel >> build_stage_3
    [build_stage_1, build_stage_2, build_stage_3] >> launch
