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

### Transpondo o DataFrame

Podemos transpor um DataFrame, transformando suas colunas em linhas e vice-versa:

```python
df_transposto = df_pessoas.T
print(df_transposto)
```