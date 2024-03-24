from airflow.models.baseoperator import BaseOperator
from duckdb_provider.hooks.duckdb_hook import DuckDBHook
from airflow.hooks.base_hook import BaseHook
import os

class PostgresToDuckDBOperator(BaseOperator):

    """
    https://github.com/apache/airflow/blob/main/airflow/models/baseoperator.py

    Essa classe define o operador customizado. Herda de BaseOperator, 
    o que significa que adota todas as funcionalidades de um operador 
    do Airflow, mas com lógica customizada definida no método execute.

    Operador que carrega um Postgres dentro de uma tabela no Duckdb.

    :param postgres_schema: Nome do schema de origem no PostgreSQL.
    :param postgres_table_name: Nome da tabela de origem no PostgreSQL e destino no DuckDB.
    :param duckdb_conn_id: ID da conexão Airflow para o DuckDB.
    :param postgres_conn_id: ID da conexão Airflow para o PostgreSQL.
    """

    def __init__(
        self,
        postgres_schema,
        postgres_table_name,
        duckdb_conn_id,
        postgres_conn_id,
        *args, **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.postgres_schema = postgres_schema
        self.postgres_table_name = postgres_table_name
        self.duckdb_conn_id = duckdb_conn_id
        self.postgresdb_conn_id = postgres_conn_id

    def execute(self, context):
        """
        Este método contém a lógica principal do operador, 
        que é executada quando a task correspondente ao operador 
        é acionada em um DAG do Airflow. Aqui está o que acontece 
        neste método:
        """
        ts = context["ts"]
        duckdb_hook = DuckDBHook(duckdb_conn_id=self.duckdb_conn_id)
        postgresql_conn = BaseHook.get_connection(self.postgresdb_conn_id)
        duckdb_conn = duckdb_hook.get_conn()
        duckdb_conn.execute("INSTALL postgres;")
        duckdb_conn.execute("LOAD postgres;")
        duckdb_conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.postgres_table_name} 
            AS SELECT * FROM postgres_scan('
                host={postgresql_conn.host} 
                user={postgresql_conn.login} 
                port=5432 
                dbname={postgresql_conn.schema} 
                password={postgresql_conn.password}', 
                '{self.postgres_schema}', 
                '{self.postgres_table_name}');""")
        query = f"""
            INSERT INTO {self.postgres_table_name} 
            SELECT * FROM postgres_scan(
                'host={postgresql_conn.host} user={postgresql_conn.login} port=5432 dbname={postgresql_conn.schema} password={postgresql_conn.password}',
                '{self.postgres_schema}',
                '{self.postgres_table_name}')
                WHERE created_at > (SELECT MAX(created_at) FROM {self.postgres_table_name});
            """
        duckdb_conn.execute(query)
        self.log.info(f"Inserted new rows into {self.postgres_table_name}")