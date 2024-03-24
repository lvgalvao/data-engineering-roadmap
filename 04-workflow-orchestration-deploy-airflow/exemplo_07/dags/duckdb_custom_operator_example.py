from airflow.decorators import dag
from pendulum import datetime
from include.custom_operators.postgres_to_duckdb_operator import PostgresToDuckDBOperator

CONNECTION_DUCKDB = "my_motherduck_conn"  # minha connection ID da MotherDuck connection
CONNECTION_POSTGRESDB = "my_postgresdb_conn" # minha connection ID do PostgreSQL connection

@dag(start_date=datetime(2024, 3, 23), schedule="*/5 * * * *", catchup=False)
def pipeline_de_migracao_postgres_to_duckdb():
    PostgresToDuckDBOperator(
        task_id="postgres_to_duckdb",
        postgres_schema="public",
        postgres_table_name="pokemons",
        duckdb_conn_id=CONNECTION_DUCKDB,
        postgres_conn_id=CONNECTION_POSTGRESDB
    )

pipeline_de_migracao_postgres_to_duckdb()
