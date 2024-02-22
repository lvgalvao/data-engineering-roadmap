# Aula 04 | Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções

Bem-vindos à quarta aula de Python e SQL focada em Engenharia de Dados. Nesta sessão, exploraremos quatro conceitos fundamentais que formam a base para o processamento e análise de dados: Listas e Dicionários, Type Hint, e Funções. Esses elementos são essenciais para a manipulação de dados, ajudando na organização, interpretação e análise eficiente das informações. 

![imagem_01](./pic/1.jpg)


Vamos começar com uma introdução a cada um desses temas para nos prepararmos para o nosso primeiro prsojeto, como ler 1 bilhão de linhas!

![imagem_05](./pic/5.jpeg)

E o nosso workshop de sabado, dia 24 as 9am, como validar 1 bilhão de linhass.

![imagem_06](./pic/6.jpeg)

## 1. Listas e Dicionários

### Importância na Engenharia de Dados

Listas e dicionários são estruturas de dados versáteis que permitem armazenar e manipular coleções de dados de forma eficiente. Na engenharia de dados, essas estruturas são fundamentais para organizar dados coletados de diversas fontes, facilitando operações como filtragem, busca, agregação e transformação de dados.

#### Exemplo: Agregação de Dados com Dicionários

Consideremos o cenário onde precisamos contar a frequência de palavras em um conjunto de dados de textos. Usando dicionários, podemos realizar essa tarefa de maneira eficiente.

```python
textos = ["engenharia de dados", "dados em python", "análise de dados"]
frequencia_palavras = {}

for texto in textos:
    palavras = texto.split()
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else:
            frequencia_palavras[palavra] = 1

print(frequencia_palavras)
```

## 2. Type Hint

### Importância na Engenharia de Dados

O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

#### Exemplo: Função de Filtragem de Dados com Type Hint

Imagine uma função que filtra dados de usuários ativos de uma lista de dicionários representando usuários. O Type Hint ajuda a garantir que os tipos de entrada e saída sejam os esperados.

```python
from typing import List, Dict

def filtrar_usuarios_ativos(usuarios: List[Dict[str, any]]) -> List[Dict[str, any]]:
    return [usuario for usuario em usuarios if usuario["ativo"]]

usuarios = [{"nome": "Alice", "ativo": True}, {"nome": "Bob", "ativo": False}, {"nome": "Carlos", "ativo": True}]
usuarios_ativos = filtrar_usuarios_ativos(usuarios)
print(usuarios_ativos)
```

## 3. Funções

### Importância na Engenharia de Dados

Funções permitem modularizar e reutilizar código, essencial para processar e analisar grandes conjuntos de dados. Na engenharia de dados, funções são usadas para encapsular lógicas de transformação, limpeza, agregação e análise de dados, tornando o código mais organizado e mantendo a qualidade do código.

#### Exemplo: Transformação de Dados com Funções

Suponhamos a necessidade de limpar e transformar nomes de usuários em um conjunto de dados. Uma função dedicada pode ser implementada para essa tarefa.

```python
def normalizar_nome(nome: str) -> str:
    return nome.strip().lower()

nomes = [" Alice ", "BOB", "Carlos"]
nomes_normalizados = [normalizar_nome(nome) for nome em nomes]
print(nomes_normalizados)
```

Cada um desses temas desempenha um papel crucial na engenharia de dados, permitindo a manipulação eficiente de dados, garantindo a qualidade do código e facilitando a análise de dados complexos. Esses exemplos ilustram como listas, dicionários, type hints e funções podem ser aplicados para resolver problemas comuns encontrados nesse campo.

## Exercicíoss

## 1. Listas e Dicionários

Listas e dicionários são estruturas de dados que permitem armazenar coleções de itens em Python. Listas são ordenadas e mutáveis, permitindo armazenar itens de diferentes tipos. Dicionários são coleções não ordenadas de pares chave-valor, permitindo armazenar e acessar dados de forma eficiente.

### Exercícios de Listas e Dicionários

1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.

## 2. Type Hint

Type hint é uma funcionalidade do Python que permite especificar o tipo de dados que uma função espera receber como argumentos, bem como o tipo de dado que ela retorna. Isso ajuda a tornar o código mais legível e facilita a detecção de erros.

### Exercícios de Type Hint

1. Escreva uma função `somar(a: int, b: int) -> int` que retorna a soma de dois números.
2. Defina uma função `concatenar(lista1: list, lista2: list) -> list` que combine duas listas.
3. Crie uma função `buscar_por_nome(pessoas: dict, nome: str) -> dict` que procure por uma pessoa em um dicionário pelo nome e retorne seus dados.
4. Escreva uma função `calcular_media(notas: list) -> float` que calcule a média de uma lista de notas.
5. Defina uma função `checar_usuario(usuario: dict) -> bool` que verifica se um dicionário possui as chaves "nome" e "ativo" e retorna `True` se ambas existirem.

## 3. Funções

Funções são blocos de código que são projetados para fazer uma tarefa específica. Em Python, uma função pode receber argumentos e pode retornar um resultado. A utilização de funções ajuda a tornar o código mais modular, reutilizável e fácil de entender.

### Exercícios de Funções

1. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
2. Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.
3. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
4. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
5. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

### Exercícios Práticos

#### 16. Eliminação de Duplicatas

**Objetivo:** Dada uma lista de emails, remover todos os duplicados.

```python
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)
```

#### 17. Filtragem de Dados

**Objetivo:** Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

```python
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)
```

#### 18. Ordenação Personalizada

**Objetivo:** Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

```python
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)
```

#### 19. Agregação de Dados

**Objetivo:** Dado um conjunto de números, calcular a média.

```python
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)
```

#### 20. Divisão de Dados em Grupos

**Objetivo:** Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

```python
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)
```

### Exercícios com Dicionários

#### 21. Atualização de Dados

**Objetivo:** Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

```python
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)
```

#### 22. Fusão de Dicionários

**Objetivo:** Dados dois dicionários, fundi-los em um único dicionário.

```python
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)
```

#### 23. Filtragem de Dados em Dicionário

**Objetivo:** Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

```python
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)
```

#### 24. Extração de Chaves e Valores

**Objetivo:** Dado um dicionário, criar listas separadas para suas chaves e valores.

```python
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)
```

#### 25. Contagem de Frequência de Itens

**Objetivo:** Dada uma string, contar a frequência de cada caractere usando um dicionário.

```python
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)
```