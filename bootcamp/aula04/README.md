# Aula 04 | Tipos complexos e Type Hint (Dicionários vs DataFrames Vs Tabelas Vs Excel)

### Exercícios com Listas

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