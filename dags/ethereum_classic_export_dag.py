from __future__ import print_function

from build_export_dag import build_export_dag
from variables import read_export_dag_vars

# airflow DAG
DAG = build_export_dag(
    dag_id='ethereum_classic_export_dag',
    **read_export_dag_vars(
        var_prefix='ethereum_classic_',
        export_schedule_interval='0 2 * * *',
        export_start_date='2015-07-30',
        export_max_workers=10,
        export_batch_size=10,
        export_daofork_traces_option=False
    )
)
