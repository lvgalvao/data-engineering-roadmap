# Aula 03: Variáveis em Python

Bem-vindo à terceira aula do curso! Hoje, vamos explorar um dos conceitos mais fundamentais da programação: variáveis. As variáveis são essenciais para armazenar e manipular dados em qualquer linguagem de programação, e em Python não é diferente. Nesta aula, vamos entender o que são variáveis, como declará-las, os tipos de dados simples suportados por Python e algumas boas práticas para nomeá-las.

## 1. Introdução às Variáveis (10 minutos)

Variáveis são espaços de memória que armazenam valores. Elas permitem que os programas armazenem e manipulem dados de forma dinâmica. No Python, as variáveis são representadas na memória associadas a endereços que contêm os valores atribuídos a elas.

**Exemplo em Python:**

```python
# Declarando e atribuindo valores às variáveis
idade = 25
altura = 1.75
nome = "João"
is_estudante = True
```

## 2. Declaração e Atribuição de Variáveis (10 minutos)

Em Python, as variáveis são declaradas simplesmente atribuindo um valor a um nome. Os valores são atribuídos às variáveis usando o operador de atribuição `=`. As variáveis podem ter seus valores alterados a qualquer momento.

**Exemplo em Python:**

```python
# Reatribuição de valores e atualização de variáveis
idade = 26
altura += 0.05
```

## 3. Tipos de Dados Simples em Python (15 minutos)

Python suporta diferentes tipos de dados simples, incluindo inteiros (`int`), números de ponto flutuante (`float`), strings (`str`) e booleanos (`bool`).

**Exemplo em Python:**

```python
# Exemplos de diferentes tipos de dados em Python
idade = 25
altura = 1.75
nome = "João"
is_estudante = True
```

## 4. Boas Práticas para Nomes de Variáveis (10 minutos)

É importante escolher nomes descritivos e significativos para suas variáveis em Python. Os nomes das variáveis devem refletir seu propósito e conteúdo, evitando nomes confusos ou genéricos.

**Exemplo em Python:**

```python
# Exemplo de nomes de variáveis significativos
idade = 25
altura = 1.75
nome_completo = "João da Silva"
```

## 5. Operadores, Conectores Lógicos e Fluxo com If (15 minutos)

Python suporta uma variedade de operadores para realizar operações matemáticas e lógicas. Os conectores lógicos, como `and`, `or` e `not`, são usados para combinar expressões booleanas. O fluxo de controle `if` é utilizado para executar blocos de código condicionalmente com base em expressões booleanas.

**Exemplo em Python:**

```python
# Exemplo de operadores e fluxo com if
idade = 25
altura = 1.75

# Verificando se a pessoa é maior de idade e tem altura suficiente para um brinquedo
if idade >= 18 and altura >= 1.50:
    print("Você pode brincar neste brinquedo.")
else:
    print("Você não atende aos requisitos para este brinquedo.")
```

**Exemplo em Python (Operadores Matemáticos):**

```python
# Exemplo de operadores matemáticos
numero1 = 10
numero2 = 5

# Operações matemáticas simples
soma = numero1 + numero2
multiplicacao = numero1 * numero2
```

**Exemplo em Python (Conectores Lógicos):**

```python
# Exemplo de conectores lógicos
tem_carteira = True
tem_dinheiro = False

# Utilizando conectores lógicos para verificar se pode dirigir
if tem_carteira and not tem_dinheiro:
    print("Você pode dirigir, mas não tem dinheiro para abastecer.")
```

## 6. Exercícios para Casa (15 minutos)

1. Escreva um programa em Python que pede ao usuário para inserir dois números e exibe o resultado da multiplicação desses números.
2. Escreva um programa em Python que verifica se um número inserido pelo usuário é par ou ímpar e exibe uma mensagem apropriada.

**Exemplo de Solução (Exercício 1):**

```python
# Exercício 1: Multiplicação de dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = numero1 * numero2
print("O resultado da multiplicação é:", resultado)
```

**Exemplo de Solução (Exercício 2):**

```python
# Exercício 2: Verificação de par ou ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

## 7. Conclusão (5 minutos)

Nesta aula, exploramos os conceitos fundamentais das variáveis em Python, incluindo declaração, atribuição, tipos de dados simples, boas práticas de nomenclatura e operadores. Compreender esses conceitos é essencial para construir programas eficazes e compreender código Python existente. Nos próximos passos, continuaremos a praticar e aprofundar nossos conhecimentos em Python.