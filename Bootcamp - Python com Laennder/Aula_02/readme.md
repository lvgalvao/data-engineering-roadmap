## Aula 02: Métodos, Funções, Pandas e Cálculos Estatísticos

### 1. Introdução aos Métodos e Funções

- **Objetivo**: Entender a diferença entre métodos e funções em Python e aprender a criar funções personalizadas.

#### O que são Métodos?

Métodos são ações associadas a um objeto em Python. Eles são definidos dentro de uma classe e operam sobre os dados do objeto. Por exemplo, o método `.upper()` transforma uma string em letras maiúsculas:

```python
texto = "hello"
print(texto.upper())  # Saída: "HELLO"
```

#### O que são Funções?

Funções são blocos de código independentes que realizam uma tarefa específica e podem retornar valores. Exemplo de uma função que soma dois números:

```python
def somar(a, b):
    return a + b

resultado = somar(3, 5)
print(f"O resultado da soma é: {resultado}")  # Saída: O resultado da soma é: 8
```

### 2. Função de Cast (Conversão de Tipos)

Casting é a conversão de um valor de um tipo para outro, como transformar uma `string` em `int` ao receber dados de um usuário via `input`:

```python
entrada = input("Digite sua idade: ")  # A entrada é uma string
idade = int(entrada)  # Converte a string para inteiro
print(f"Sua idade é: {idade}")
```

### 3. Criando Funções Personalizadas

Agora, vamos criar funções para calcular **média**, **variância** e **desvio padrão** de uma lista de números.

#### Função para Calcular a Média:

A média é o valor central de um conjunto de números:

```python
def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media
```

#### Função para Calcular a Variância:

A variância mede a dispersão dos valores em relação à média:

```python
def calcular_variancia(lista):
    media = calcular_media(lista)
    soma_diferencas = 0
    for valor in lista:
        diferenca = valor - media
        soma_diferencas += diferenca ** 2
    variancia = soma_diferencas / len(lista)
    return variancia
```

#### Função para Calcular o Desvio Padrão:

O desvio padrão é a raiz quadrada da variância, medindo a dispersão dos valores:

```python
def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao
```

### 4. Aplicação Prática

Vamos aplicar essas funções a uma lista de idades:

```python
idades = [23, 29, 31, 25]

media = calcular_media(idades)
variancia = calcular_variancia(idades)
desvio_padrao = calcular_desvio_padrao(idades)

print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
```

---

## Simplificando com pandas

Agora que calculamos as estatísticas manualmente, podemos simplificar o processo usando o **pandas**, uma biblioteca poderosa para manipulação de dados. Vamos explorar como usar pandas para realizar esses cálculos automaticamente.

### 1. **Média** (`mean`)

A **média** é o valor central de um conjunto de dados.

```python
media = idades_series.mean()
print(f"Média: {media}")
```

### 2. **Mediana** (`median`)

A **mediana** é o valor central de um conjunto ordenado de dados.

```python
mediana = idades_series.median()
print(f"Mediana: {mediana}")
```

### 3. **Desvio Padrão** (`std`)

O **desvio padrão** mede o quão dispersos os valores estão em relação à média.

```python
desvio_padrao = idades_series.std()
print(f"Desvio Padrão: {desvio_padrao}")
```

### 4. **Variância** (`var`)

A **variância** é a medida da dispersão ao quadrado dos valores em relação à média.

```python
variancia = idades_series.var()
print(f"Variância: {variancia}")
```

### 5. **Moda** (`mode`)

A **moda** é o valor que ocorre com mais frequência.

```python
moda = idades_series.mode()[0]
print(f"Moda: {moda}")
```

### 6. **Quartis** (`quantile`)

Os **quartis** dividem os dados em quatro partes iguais.

```python
primeiro_quartil = idades_series.quantile(0.25)
terceiro_quartil = idades_series.quantile(0.75)
print(f"Primeiro Quartil: {primeiro_quartil}")
print(f"Terceiro Quartil: {terceiro_quartil}")
```

### 7. Outros Métodos Estatísticos

#### Mínimo e Máximo:

```python
minimo = idades_series.min()
maximo = idades_series.max()
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
```

#### Soma e Contagem:

```python
soma = idades_series.sum()
contagem = idades_series.count()
print(f"Soma: {soma}")
print(f"Contagem: {contagem}")
```

---

## Explorando Outros Métodos e Atributos do pandas

### 1. Método `describe`

O método `describe` fornece um resumo estatístico da série.

```python
resumo = idades_series.describe()
print(resumo)
```

### 2. Atributo `shape`

O atributo `shape` retorna as dimensões da série.

```python
forma = idades_series.shape
print(f"Forma da Série: {forma}")
```

### 3. Índices e `iloc`

Cada elemento em uma série tem um índice associado, que pode ser acessado diretamente:

```python
# Acessando valor pelo índice
valor_no_indice_2 = idades_series[2]
print(f"Valor no índice 2: {valor_no_indice_2}")

# Usando iloc para acessar pela posição
valor_posicao_1 = idades_series.iloc[1]
print(f"Valor na posição 1: {valor_posicao_1}")
```

### 4. Nomeando Séries

Podemos dar um nome à série usando o atributo `name`:

```python
idades_series.name = "Idades dos Participantes"
print(idades_series)
```

---

## Conclusão: DataFrame é um Conjunto de Séries

Um **DataFrame** no pandas é uma coleção de **Séries**. Cada coluna de um DataFrame é uma Série, e as linhas compartilham o mesmo índice. Vamos criar um DataFrame a partir de Séries:

```python
serie_nomes = pd.Series(["Ana", "Bruno", "Carla", "David"])
serie_sobrenomes = pd.Series(["Silva", "Oliveira", "Santos", "Costa"])
serie_idades = pd.Series([23, 29, 31, 25])

df_pessoas = pd.DataFrame({
    "nome": serie_nomes,
    "sobrenome": serie_sobrenomes,
    "idade": serie_idades
})

print(df_pessoas)
```

### Acessando Séries de um DataFrame

Podemos acessar uma coluna específica (Série) de um DataFrame da seguinte forma:

```python
serie_nomes_do_df = df_pessoas["nome"]
print(serie_nomes_do_df)
```

### Aula: Manipulação de DataFrames com Pandas e Integração de Múltiplos Arquivos CSV

Nesta aula, vamos trabalhar com três arquivos CSV de **vendas** e um arquivo CSV de **clientes**, aplicando as operações mais comuns do pandas, como **leitura**, **join**, **agregação**, **filtragem** e **salvamento**. O foco será entender como integrar múltiplas fontes de dados e fazer análises.

#### Arquivos CSV:
- **clientes.csv**: Arquivo contendo a dimensão dos clientes, com 10 linhas e informações pessoais dos clientes.
- **vendas.csv**: Arquivo contendo 100 vendas.
- **vendas_2.csv**: Segundo arquivo de vendas com mais 100 vendas.
- **vendas_3.csv**: Terceiro arquivo de vendas com 100 vendas adicionais.

### Estrutura dos Arquivos

#### 1. **clientes.csv** (Dimensão)
Colunas:
- `cliente_id`: Chave primária.
- `nome`: Nome do cliente.
- `sobrenome`: Sobrenome do cliente.
- `cidade`: Cidade de residência.
- `idade`: Idade do cliente.
- `email`: Endereço de email.

#### 2. **vendas.csv**, **vendas_2.csv**, **vendas_3.csv** (Fato)
Colunas:
- `venda_id`: ID único da venda.
- `cliente_id`: Chave estrangeira para relacionar com a tabela de clientes.
- `produto`: Produto vendido.
- `quantidade`: Quantidade vendida.
- `valor_unitario`: Preço por unidade do produto.
- `data_venda`: Data da venda.

### Passo a Passo: Manipulação de DataFrames com Pandas

#### Passo 1: Leitura dos Arquivos CSV

Vamos começar lendo os três arquivos de vendas e o arquivo de clientes usando `pd.read_csv()`.

```python
import pandas as pd

# Leitura dos CSVs de clientes e vendas
df_clientes = pd.read_csv('clientes.csv')
df_vendas = pd.read_csv('vendas.csv')
df_vendas_2 = pd.read_csv('vendas_2.csv')
df_vendas_3 = pd.read_csv('vendas_3.csv')

# Exibindo as primeiras linhas de cada DataFrame
print(df_clientes.head())
print(df_vendas.head())
print(df_vendas_2.head())
print(df_vendas_3.head())
```

#### Passo 2: Unindo os Arquivos de Vendas

Agora, vamos combinar os três DataFrames de vendas em um único DataFrame usando `pd.concat()`. Isso vai consolidar todas as 300 vendas.

```python
# Unindo as três tabelas de vendas
df_todas_vendas = pd.concat([df_vendas, df_vendas_2, df_vendas_3])

# Exibindo o DataFrame combinado
print(df_todas_vendas.shape)  # Verificar o número total de vendas (deve ser 300)
print(df_todas_vendas.head())
```

#### Passo 3: Fazendo o Join entre Vendas e Clientes

Agora que temos um DataFrame com todas as vendas, vamos juntar (fazer o **join**) com a tabela de clientes usando a coluna `cliente_id`, que está presente em ambos os DataFrames.

```python
# Fazendo o join entre o DataFrame de vendas e o de clientes
df_completo = pd.merge(df_todas_vendas, df_clientes, on="cliente_id")

# Exibindo o DataFrame resultante
print(df_completo.head())
```

#### Passo 4: Análise Exploratória

Agora que temos o DataFrame completo, vamos fazer algumas análises:

- **Número total de vendas**:
```python
total_vendas = df_completo['venda_id'].count()
print(f"Total de vendas: {total_vendas}")
```

- **Valor total vendido**:
Vamos calcular o valor total das vendas (quantidade * valor_unitário):

```python
df_completo['valor_total'] = df_completo['quantidade'] * df_completo['valor_unitario']
valor_total = df_completo['valor_total'].sum()
print(f"Valor total vendido: {valor_total}")
```

- **Média do valor por venda**:
```python
media_venda = df_completo['valor_total'].mean()
print(f"Média por venda: {media_venda}")
```

#### Passo 5: Agrupamento e Resumo de Vendas

Vamos agrupar as vendas por cliente e calcular o total de vendas por cada cliente:

- **Total de vendas por cliente**:
```python
vendas_por_cliente = df_completo.groupby('nome')['valor_total'].sum()
print(vendas_por_cliente)
```

- **Número de vendas por produto**:
```python
vendas_por_produto = df_completo.groupby('produto')['venda_id'].count()
print(vendas_por_produto)
```

#### Passo 6: Filtragem dos Dados

Agora, vamos filtrar o DataFrame para analisar as vendas de um cliente específico ou as vendas realizadas em uma cidade específica.

- **Vendas de clientes da cidade de São Paulo**:
```python
vendas_sp = df_completo[df_completo['cidade'] == 'São Paulo']
print(vendas_sp)
```

- **Vendas de um cliente específico (por exemplo, 'Ana')**:
```python
vendas_ana = df_completo[df_completo['nome'] == 'Ana']
print(vendas_ana)
```

#### Passo 7: Ordenação das Vendas

Vamos ordenar as vendas pelo maior valor total de venda:

```python
vendas_ordenadas = df_completo.sort_values(by='valor_total', ascending=False)
print(vendas_ordenadas.head())
```

#### Passo 8: Salvando o DataFrame Resultante

Após todas as manipulações, podemos salvar o DataFrame resultante em um novo arquivo CSV para análise futura:

```python
df_completo.to_csv('vendas_completo.csv', index=False)
```

### Resumo das Operações Realizadas:

- **Leitura de CSVs**: Importação dos dados de clientes e vendas.
- **Concatenação**: Unindo múltiplos DataFrames de vendas em um único DataFrame.
- **Merge/Join**: Juntando os dados de clientes com as vendas através da coluna `cliente_id`.
- **Cálculos**: Realizando operações de soma, média e agregações sobre as vendas.
- **Agrupamento**: Agrupando vendas por cliente e por produto.
- **Filtragem**: Selecionando dados com base em critérios, como cidade ou cliente.
- **Ordenação**: Ordenando os dados para identificar as maiores vendas.
- **Salvamento**: Exportando o DataFrame resultante para um novo CSV.

Sim, o pandas permite salvar os dados diretamente em um banco de dados relacional usando a função **`to_sql()`**, que possibilita gravar os dados de um **DataFrame** em tabelas de um banco de dados. Para isso, você pode utilizar bibliotecas como **SQLAlchemy** para criar uma conexão com o banco de dados.

Aqui está um exemplo básico de como você pode salvar um DataFrame em um banco de dados usando pandas:

### 1. Instale as Dependências

Primeiro, você precisa instalar o **SQLAlchemy** e o conector específico para o banco de dados que você está usando (por exemplo, **psycopg2** para PostgreSQL, **PyMySQL** para MySQL, etc.).

```bash
pip install sqlalchemy
pip install psycopg2  # Para PostgreSQL
pip install pymysql   # Para MySQL
```

### 2. Código para Salvar o DataFrame em um Banco de Dados

Vamos usar o **SQLAlchemy** para criar uma conexão com o banco de dados e, em seguida, usar a função **`to_sql()`** do pandas para salvar os dados.

#### Exemplo: Salvando em um Banco de Dados PostgreSQL

```python
import pandas as pd
from sqlalchemy import create_engine

# Supondo que df_completo seja o DataFrame resultante que você quer salvar
# Configurar a conexão com o banco de dados
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/nome_do_banco')

# Salvando o DataFrame 'df_completo' na tabela 'vendas_completo' do banco de dados
df_completo.to_sql('vendas_completo', engine, if_exists='replace', index=False)

print("Dados salvos no banco de dados com sucesso!")
```

### Explicação:

- **`create_engine()`**: Cria a conexão com o banco de dados usando a string de conexão. Você precisa ajustar o `username`, `password`, `localhost`, `5432` (porta) e `nome_do_banco` para refletir suas credenciais e configurações do banco.
  
- **`to_sql()`**:
  - O primeiro argumento é o nome da tabela onde os dados serão inseridos (`vendas_completo`).
  - O segundo argumento é a conexão (`engine`).
  - `if_exists='replace'` indica que, se a tabela já existir, ela será substituída. Você pode usar `'append'` para adicionar dados a uma tabela já existente.
  - `index=False` evita que o índice do DataFrame seja salvo como uma coluna na tabela.