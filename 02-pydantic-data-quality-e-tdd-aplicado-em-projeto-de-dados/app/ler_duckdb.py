import duckdb

def read_from_duckdb_and_print(table_name: str, db_file: str = 'my_duckdb.db'):
    """
    Lê dados de uma tabela DuckDB e imprime os resultados.

    Parâmetros:
    - table_name: Nome da tabela de onde os dados serão lidos.
    - db_file: Caminho para o arquivo DuckDB.
    """
    # Conectar ao DuckDB
    con = duckdb.connect(database=db_file)

    # Executar consulta SQL
    query = f"SELECT * FROM {table_name}"
    result = con.execute(query).fetchall()

    # Fechar a conexão
    con.close()

    # Imprimir os resultados
    for row in result:
        print(row)

if __name__ == "__main__":
    # Nome da tabela para consulta
    table_name = "tabela_kpi"
    
    # Ler dados da tabela e imprimir os resultados
    read_from_duckdb_and_print(table_name)