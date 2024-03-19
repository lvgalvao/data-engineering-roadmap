# Aula 17: SQLAlchemy - Conjunto de ferramentas para manipular SQL em 

![imagem_01](./pics/1.jpg)

Bem-vindo à décima sétima aula do bootcamp!

Mapeamento Objeto-Relacional (ORM) é uma técnica que permite consultar e manipular dados de um banco de dados usando um paradigma orientado a objetos. Ao falar sobre ORM, a maioria das pessoas está se referindo a uma biblioteca que implementa a técnica de Mapeamento Objeto-Relacional, daí a frase "um ORM".

[Excalidraw:](https://link.excalidraw.com/l/8pvW6zbNUnD/3tmGeQYjxeG)

## Introdução ao SQL Alchemy

Uma biblioteca ORM é uma biblioteca completamente comum escrita na linguagem de sua escolha que encapsula o código necessário para manipular os dados, então você não usa mais SQL; você interage diretamente com um objeto na mesma linguagem que está usando.

### Por que devemos usar ORM?

- DRY: Você escreve seu modelo de dados em apenas um lugar, e é mais fácil atualizar, manter e reutilizar o código.

- Você não precisa escrever seu SQL zoado (a maioria dos programadores não são bons nisso, porque SQL é tratado como uma "sub" linguagem, quando na realidade é uma linguagem muito poderosa e complexa).

- Sanitização; usar declarações preparadas ou transações é tão fácil quanto chamar um método.

- Ela se encaixa na sua maneira natural no seu código Python.

- Ela abstrai o sistema de BD, então você pode mudá-lo sempre que quiser.

![imagem_02](./pics/2.jpg)

### Instalação

Primeiro, certifique-se de que o SQLAlchemy esteja instalado. Se não estiver, você pode instalá-lo usando pip:

```bash
pip install sqlalchemy
```

### Conectando ao SQLite (Hello world!)

SQLite é um banco de dados leve que é ótimo para aprender os fundamentos do SQLAlchemy. Aqui está um exemplo básico de como criar uma engine de conexão com um banco de dados SQLite em memória:

```python
from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")
```

![engine](./pics/engine.png)

[Atende diferentes "Dialect"](https://docs.sqlalchemy.org/en/20/core/engines.html)  

### Criando nosso MAPPING

![engine](./pics/mapping.png)


Antes de inserir ou consultar dados, precisamos definir os modelos e criar tabelas correspondentes no banco de dados:

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)
```

### Criando Sessões e Inserindo Dados

As sessões no SQLAlchemy são usadas para manter um 'workspace' de todas as operações de objetos que você deseja sincronizar com o banco de dados:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")
```

### Consultando Dados

Agora, vamos consultar os dados para verificar a inserção:

```python
usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")
```

### Utilizando Session com o With

O gerenciador de contexto `with` em Python, especialmente quando usado com SQLAlchemy, é uma maneira elegante e segura de garantir que os recursos, como conexões de banco de dados e sessões, sejam apropriadamente gerenciados. Ao usar o `with`, você se beneficia da entrada e saída automática de contextos, o que significa que ao final do bloco `with`, o SQLAlchemy automaticamente fecha a sessão ou faz o commit/rollback, dependendo do resultado da operação. Isso ajuda a prevenir vazamentos de conexão e garante que as transações sejam devidamente gerenciadas.

### Vantagens do Uso do `with` com SQLAlchemy

* **Gerenciamento automático de transações**: As transações são automaticamente commitadas ou revertidas dependendo se exceções foram lançadas dentro do bloco.
* **Fechamento automático de sessões**: Isso garante que os recursos sejam liberados de maneira oportuna, evitando vazamentos de conexão.

### Exemplo Sem Usar `with`

Sem utilizar o gerenciador de contexto, você precisa manualmente gerenciar a sessão, incluindo commits, rollbacks e o fechamento da sessão:

```python
from sqlalchemy.orm import sessionmaker
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
session = Session()

try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
```

Neste exemplo, todos os passos para garantir que a sessão seja devidamente gerida são explícitos: comitar as alterações, lidar com exceções, fazer rollback se algo der errado, e, por fim, fechar a sessão.

### Exemplo Usando `with`

Quando você utiliza o gerenciador de contexto `with`, muitas dessas etapas são automatizadas:

```python
from sqlalchemy.orm import sessionmaker, Session
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with
```

No exemplo acima, o SQLAlchemy lida com o commit, rollback e fechamento da sessão automaticamente. Se uma exceção ocorrer dentro do bloco `with`, um rollback é chamado. Quando o bloco `with` é concluído sem erros, o commit é realizado, e em ambos os casos, a sessão é fechada automaticamente no final.

### Conclusão

A principal vantagem de usar o gerenciador de contexto `with` com SQLAlchemy (ou qualquer outro recurso que necessite de gerenciamento de estado e liberação de recursos) é reduzir a verbosidade do código e minimizar a chance de erros, como esquecer de fechar uma sessão ou fazer rollback de uma transação falha. Ele promove um código mais limpo, seguro e legível.

### Desafio

![imagem_03](./pics/3.jpg)

### Desafio Intermediário de SQLAlchemy: Tabelas de Produto e Fornecedor

Este desafio focará na criação de duas tabelas relacionadas, `Produto` e `Fornecedor`, utilizando SQLAlchemy. Cada produto terá um fornecedor associado, demonstrando o uso de chaves estrangeiras para estabelecer relações entre tabelas. Além disso, você realizará inserções nessas tabelas para praticar a manipulação de dados.

#### Passo 1: Configuração Inicial

Primeiro, certifique-se de ter o SQLAlchemy instalado. Se não, instale-o usando pip:

```bash
pip install sqlalchemy
```

#### Passo 2: Definição dos Modelos

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    
    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")
```

#### Passo 3: Criando o Banco de Dados e as Tabelas

```python
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

#### Passo 4: Inserções nas Tabelas

Primeiro, vamos inserir alguns fornecedores:

```python
fornecedores = [
    Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
    Fornecedor(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
    Fornecedor(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
    Fornecedor(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
    Fornecedor(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
]

session.add_all(fornecedores)
session.commit()
```

Em seguida, inserimos alguns produtos, cada um vinculado a um fornecedor:

```python
produtos = [
    Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
    Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
    Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
    Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
    Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
]

session.add_all(produtos)
session.commit()
```

#### Passo 5: Consulta dos Dados

Para verificar se tudo correu como esperado, você pode fazer uma consulta simples para listar todos os produtos e seus fornecedores:

```python
for produto in session.query(Produto).all():
    print(f"Produto: {produto.nome}, Fornecedor: {produto.fornecedor.nome}")
```

Este desafio cobre conceitos intermediários como a criação de tabelas relacionadas, inserção de dados com chaves estrangeiras e consultas básicas no SQLAlchemy. Ele oferece uma boa prática para quem está aprendendo a manipular relações entre tabelas em um contexto de banco de dados relacional usando ORM.

Vamos criar um exemplo prático que demonstra a utilização de `JOIN` e `GROUP BY` tanto em SQL puro quanto usando o SQLAlchemy (ORM). O objetivo é obter a soma dos preços dos produtos agrupados por fornecedor.

### Cenário

Temos duas tabelas: `fornecedores` e `produtos`. Cada produto tem um `fornecedor_id` que o vincula a um fornecedor específico na tabela `fornecedores`.

### SQL Puro

Para realizar essa operação em SQL puro, você pode usar a seguinte query:

```sql
SELECT fornecedores.nome, SUM(produtos.preco) AS total_preco
FROM produtos
JOIN fornecedores ON produtos.fornecedor_id = fornecedores.id
GROUP BY fornecedores.nome;
```

Esta query junta as tabelas `produtos` e `fornecedores` através do `fornecedor_id`, agrupa os resultados pelo nome do fornecedor e, para cada grupo, calcula a soma dos preços dos produtos associados a esse fornecedor.

### SQLAlchemy (ORM)

Para realizar a mesma operação usando SQLAlchemy, você seguiria estes passos:

```python
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")
```

No exemplo acima com SQLAlchemy, utilizamos o método `query()` para construir uma consulta que seleciona o nome do fornecedor e a soma dos preços dos produtos. Usamos `join()` para juntar as tabelas `Produto` e `Fornecedor` baseadas na chave estrangeira. `group_by()` é utilizado para agrupar os resultados pelo nome do fornecedor, e `func.sum()` calcula a soma dos preços dos produtos para cada grupo.

### Conclusão

Ambos os métodos, SQL puro e SQLAlchemy, alcançam o mesmo resultado: agrupam os produtos por fornecedor e calculam a soma dos preços dos produtos para cada fornecedor. A principal diferença está na abordagem: enquanto o SQL puro é mais direto e requer que você escreva a query explicitamente, o SQLAlchemy abstrai a construção da query, permitindo que você utilize métodos Python e relações entre modelos para definir a consulta. A escolha entre um ou outro dependerá das suas necessidades específicas, preferências de desenvolvimento e o contexto do seu projeto.