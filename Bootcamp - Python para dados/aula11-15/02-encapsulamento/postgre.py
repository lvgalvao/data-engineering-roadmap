import psycopg2

class BancoDeDadosPost:
    def __init__(self, host, porta, banco, usuario, senha):
        self.host = host
        self.porta = porta
        self.banco = banco
        self.usuario = usuario
        self.senha = senha
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                port=self.porta,
                database=self.banco,
                user=self.usuario,
                password=self.senha
            )
            print("Conexão estabelecida com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def executar_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executada com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao executar a query:", e)


# Exemplo de uso
if __name__ == "__main__":
    host = 'localhost'
    porta = '5432'
    banco = 'nome_do_banco'
    usuario = 'usuario'
    senha = 'senha'
    
    banco = BancoDeDadosPost(host, porta, banco, usuario, senha)
    banco.conectar()

    # Exemplo de criação de tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """
    banco.executar_query(create_table_query)

    # Exemplo de inserção de dados
    insert_query = """
    INSERT INTO usuarios (nome, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    banco.executar_query(insert_query)

    banco.desconectar()
