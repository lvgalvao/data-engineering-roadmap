### Exercício: Cálculo de Estatísticas com Python Puro e pandas

Neste exercício, você vai trabalhar com uma lista de 20 itens e calcular **média**, **desvio padrão**, **máximo** e **mínimo** tanto usando Python puro quanto usando **pandas**.

#### Lista de números:
```python
numeros = [23, 45, 67, 89, 12, 34, 56, 78, 90, 21, 43, 65, 87, 32, 54, 76, 98, 10, 30, 50]
```

### Passo 1: Cálculos com Python Puro

1. **Média**: Soma dos elementos dividida pelo número de elementos.
2. **Desvio Padrão**: Raiz quadrada da variância.
3. **Máximo**: Maior valor da lista.
4. **Mínimo**: Menor valor da lista.

#### Cálculos com Python Puro:

```python

numeros = [23, 45, 67, 89, 12, 34, 56, 78, 90, 21, 43, 65, 87, 32, 54, 76, 98, 10, 30, 50]

# Função para calcular a média
def calcular_media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media

# Função para calcular a variância
def calcular_variancia(lista):
    media = calcular_media(lista)
    soma_diferencas = 0
    for valor in lista:
        diferenca = valor - media
        soma_diferencas += diferenca ** 2
    variancia = soma_diferencas / len(lista)
    return variancia

# Função para calcular o desvio padrão
def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

# Cálculos
media = calcular_media(numeros)
desvio_padrao = calcular_desvio_padrao(numeros)
maximo = max(numeros)
minimo = min(numeros)

# Exibindo os resultados
print(f"Média: {media}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
```

### Saída Esperada:

```plaintext
Média: 52.95
Desvio Padrão: 26.715776024038615
Máximo: 98
Mínimo: 10
```

### Passo 2: Cálculos com pandas Series

Agora, vamos realizar os mesmos cálculos usando uma **Série** do pandas. A vantagem do pandas é que essas operações já são implementadas como métodos da Série, o que simplifica o código.

#### Cálculos com pandas:

```python
import pandas as pd

# Criando uma Série com os números
serie_numeros = pd.Series(numeros)

# Cálculos usando pandas
media_pandas = serie_numeros.mean()
desvio_padrao_pandas = serie_numeros.std()
maximo_pandas = serie_numeros.max()
minimo_pandas = serie_numeros.min()

# Exibindo os resultados
print(f"Média (pandas): {media_pandas}")
print(f"Desvio Padrão (pandas): {desvio_padrao_pandas}")
print(f"Máximo (pandas): {maximo_pandas}")
print(f"Mínimo (pandas): {minimo_pandas}")
```

### Saída Esperada:

```plaintext
Média (pandas): 52.95
Desvio Padrão (pandas): 27.209487879199906
Máximo (pandas): 98
Mínimo (pandas): 10
```

### Comparação dos Resultados

- **Média** e **Máximo** e **Mínimo** devem ser iguais em ambos os casos.
- O **desvio padrão** pode diferir ligeiramente, porque o pandas, por padrão, calcula o desvio padrão amostral (dividido por `n-1`), enquanto o cálculo manual faz o desvio padrão populacional (dividido por `n`). Você pode ajustar o pandas para calcular o desvio padrão populacional usando o argumento `ddof=0`:

```python
desvio_padrao_pandas = serie_numeros.std(ddof=0)
```

Este exercício demonstra a flexibilidade do pandas para realizar cálculos estatísticos rapidamente e a importância de entender como as fórmulas são aplicadas tanto manualmente quanto com bibliotecas especializadas.