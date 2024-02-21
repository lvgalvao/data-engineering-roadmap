# Aula 05: Estrutura de Dados (Parte 2) - Dicionários e Conjuntos

Bem-vindo à quarta aula do curso! Nesta aula, continuaremos nossa exploração das estruturas de dados em Python, desta vez focando em dicionários e conjuntos. Essas estruturas são fundamentais para lidar com dados de forma eficiente e organizada, e entender como usá-las é essencial para qualquer programador Python.

## Objetivos

* Compreender o conceito de dicionários e conjuntos em Python.
* Aprender a criar, acessar e manipular dicionários e conjuntos.
* Explorar os métodos e operações disponíveis para dicionários e conjuntos.

## Agenda

1. Introdução aos Dicionários (10 minutos)
2. Operações com Dicionários (15 minutos)
3. Introdução aos Conjuntos (10 minutos)
4. Operações com Conjuntos (15 minutos)
5. Exemplos Práticos (20 minutos)
6. Conclusão (5 minutos)

## 1. Introdução aos Dicionários (10 minutos)

* **O que são dicionários?**
    * Dicionários são estruturas de dados que armazenam pares chave-valor.
* **Por que os dicionários são importantes?**
    * Permitem associar informações entre chaves e valores de forma eficiente.
* **Como os dicionários são representados?**
    * Os dicionários são representados por chaves `{}` e contêm pares chave-valor separados por vírgulas.

Exemplo em Python:

```python
# Exemplo de criação de um dicionário
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
```

## 2. Operações com Dicionários (15 minutos)

* **Acesso a elementos por chave.**
* **Adição e remoção de elementos.**
* **Atualização de valores.**
* **Métodos úteis para dicionários, como `keys()`, `values()` e `items()`.**

Exemplo em Python:

```python
# Acesso a elementos por chave
print(pessoa["nome"])  # Saída: João

# Adição de um novo elemento
pessoa["profissão"] = "Engenheiro"

# Remoção de um elemento
del pessoa["idade"]

# Atualização de valores
pessoa["cidade"] = "Rio de Janeiro"

# Métodos úteis para dicionários
print(pessoa.keys())  # Saída: dict_keys(['nome', 'cidade', 'profissão'])
```

## 3. Introdução aos Conjuntos (10 minutos)

* **O que são conjuntos em Python?**
    * Conjuntos são coleções não ordenadas de elementos únicos.
* **Por que os conjuntos são úteis?**
    * Permitem verificar a presença de elementos e realizar operações de conjunto de forma eficiente.

Exemplo em Python:

```python
# Exemplo de criação de um conjunto
numeros = {1, 2, 3, 4, 5}
```

## 4. Operações com Conjuntos (15 minutos)

* **Adição e remoção de elementos.**
* **Verificação de pertencimento.**
* **Operações de conjunto, como união, interseção e diferença.**

Exemplo em Python:

```python
# Adição de um novo elemento
numeros.add(6)

# Remoção de um elemento
numeros.remove(5)

# Verificação de pertencimento
print(3 in numeros)  # Saída: True

# Operações de conjunto
pares = {2, 4, 6, 8, 10}
print(numeros.union(pares))  # Saída: {1, 2, 3, 4, 6, 8, 10}
```

## 5. Exemplos Práticos (20 minutos)

* **Manipulação de dados utilizando dicionários e conjuntos.**
* **Aplicações práticas de operações de dicionários e conjuntos.**

Exemplo em Python:

```python
# Exemplo prático: contagem de palavras em um texto
texto = "Python é uma linguagem de programação poderosa e fácil de aprender."
palavras = texto.split()
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)
```

## 6. Conclusão (5 minutos)

* **Recapitulação dos principais conceitos abordados.**
* **Importância de dicionários e conjuntos na programação Python.**
* **Próximos passos: prática e aprofundamento nos conceitos de dicionários e conjuntos.**

### Desafio 1: Contagem de Palavras

Escreva um programa em Python que recebe um texto como entrada e conta quantas vezes cada palavra aparece no texto. Utilize um dicionário para armazenar a contagem de palavras e ignore maiúsculas e minúsculas (ou seja, considere "Python" e "python" como a mesma palavra).

#### Exemplo de Entrada:

```python
texto = "Python é uma linguagem de programação poderosa e fácil de aprender. Python é amplamente utilizado em diversas áreas, incluindo desenvolvimento web, ciência de dados e automação."
```

#### Saída Esperada:

```python
{
    "python": 2,
    "é": 1,
    "uma": 1,
    "linguagem": 1,
    "de": 2,
    "programação": 1,
    "poderosa": 1,
    "e": 2,
    "fácil": 1,
    "aprender": 1,
    "amplamente": 1,
    "utilizado": 1,
    "em": 1,
    "diversas": 1,
    "áreas": 1,
    "incluindo": 1,
    "desenvolvimento": 1,
    "web": 1,
    "ciência": 1,
    "dados": 1,
    "automação": 1
}
```

### Desafio 2: Verificação de Anagramas

Um anagrama é uma palavra ou frase formada pela reorganização das letras de outra palavra ou frase, utilizando todas as letras originais exatamente uma vez. Escreva uma função em Python que recebe duas strings como entrada e verifica se são anagramas uma da outra, ou seja, se uma pode ser formada pela reorganização das letras da outra.

#### Exemplo de Entrada:

```python
palavra1 = "listen"
palavra2 = "silent"
```

#### Saída Esperada:

```python
True
```

#### Exemplo de Entrada:

```python
palavra1 = "hello"
palavra2 = "world"
```

#### Saída Esperada:

```python
False
```

### Instruções:

1. Implemente as soluções para os desafios propostos em um arquivo Python separado.
2. Certifique-se de que seu código está devidamente comentado e organizado.
3. Teste suas soluções com diferentes entradas para garantir que funcionam corretamente.
4. Entregue seu código até o próximo encontro para discussão e revisão em sala de aula.