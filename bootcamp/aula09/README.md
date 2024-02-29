# Aula 09: Funções em Python - Decoradores

Na engenharia de dados, a eficiência, reusabilidade e confiabilidade do código são cruciais. Por isso, trabalhamos com decoradores.

![imagem_01](./pic/1.jpg)

**Usando LOG**

Quando queremos entender mais sobre nossa aplicação, temos duas alternativas.

- Utilizar o Print
- Utilizar o Debugger

Hoje quero apresentar uma terceira opção, que é o logging.

[![imagem_05](./pic/5.png)](https://www.linkedin.com/posts/lucianovasconcelosf_voc%C3%A9-%C3%A9-da-turma-do-print-ou-do-log-debugar-activity-7166127525763518464-z8AN?utm_source=share&utm_medium=member_desktop)

## Conteúdo

![imagem_02](./pic/2.jpg)

O Loguru é uma biblioteca de logging para Python que visa trazer uma experiência de uso mais simples e poderosa do que o módulo de logging padrão do Python. Com uma API simples, Loguru oferece várias funcionalidades úteis, como rotação de arquivos, serialização JSON, envio de mensagens para múltiplos destinos, e muito mais, tudo isso sem a necessidade de configuração inicial complicada.

### O que é Logging?

Logging é o processo de gravar mensagens que documentam os eventos que ocorrem durante a execução de um software. Essas mensagens podem indicar progresso da execução, falhas, erros, ou outras informações úteis. O logging é crucial para desenvolvimento e manutenção de software, pois permite aos desenvolvedores e administradores de sistema entender o que o aplicativo está fazendo, diagnosticar problemas e monitorar o desempenho em produção.

### Como Utilizar o Loguru

Para começar a usar o Loguru, você primeiro precisa instalá-lo. Isso pode ser feito facilmente via pip:

```bash
poetry add loguru
```

Agora, vamos aos exemplos de como utilizar o Loguru em seu código Python.

#### Exemplo 1: Logging Básico

Este exemplo mostra como fazer logging básico com Loguru

```python
from loguru import logger

logger.info("Isso é uma mensagem informativa")

# A saída será exibida no console
```

#### Exemplo 2: Configuração de Arquivo de Log

Aqui, configuramos o Loguru para salvar mensagens de log em um arquivo, incluindo a rotação do arquivo baseada no tamanho.

```python
from loguru import logger

# Configurando o arquivo de log com rotação de 5MB
logger.add("meu_app.log", rotation="5 MB")

logger.info("Essa mensagem será salva no arquivo")
```

No exemplo acima, `logger.add()` é usado para adicionar um "sink" (destino) que, neste caso, é um arquivo. A opção `rotation` determina que um novo arquivo será criado sempre que o atual atingir 5MB.

#### Exemplo 3: Capturando e salvando

Aqui está um exemplo de como configurar o `loguru` para salvar os logs tanto em um arquivo quanto exibi-los na saída padrão (`stderr`):

```python
from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")
```

Neste código, dois "sinks" são adicionados ao `logger`:

1. `stderr`, para exibir os logs, com uma formatação específica que inclui o tempo, nível de log, mensagem e arquivo de origem.

2. `"meu_arquivo_de_logs.log"`, para salvar os logs em um arquivo com uma formatação que também inclui tempo, nível, mensagem e arquivo de origem.

Os níveis de log em Python (e em muitos sistemas de logging em outras linguagens de programação) são usados para indicar a gravidade ou importância das mensagens registradas pelo aplicativo. Eles ajudam a diferenciar entre tipos de informações que estão sendo logadas, permitindo uma filtragem e análise mais eficazes dos dados de log. Aqui estão os níveis de log mais comuns, listados em ordem crescente de gravidade:

### DEBUG

* **Descrição**: O nível DEBUG é usado para informações detalhadas, tipicamente de interesse apenas quando se está diagnosticando problemas.
* **Uso**: Desenvolvedores usam este nível para obter informações detalhadas sobre o fluxo da aplicação, variáveis de estado, e para entender como o código está operando durante o desenvolvimento e a depuração.

### INFO

* **Descrição**: O nível INFO é usado para confirmar que as coisas estão funcionando conforme o esperado.
* **Uso**: Este nível é geralmente o padrão em produção para registrar eventos normais do sistema, como processos de inicialização, operações concluídas com sucesso, ou outras transações de rotina.

### WARNING

* **Descrição**: O nível WARNING indica que algo inesperado aconteceu, ou indica algum problema no futuro próximo (e.g., 'disco quase cheio'). O software está funcionando como esperado.
* **Uso**: Utiliza-se este nível para alertar sobre situações que podem necessitar de atenção mas não impedem o funcionamento do sistema. Por exemplo, usar uma função obsoleta ou problemas de performance que não requerem uma ação imediata.

### ERROR

* **Descrição**: O nível ERROR indica que devido a um problema mais grave, a execução de alguma função ou operação falhou.
* **Uso**: Este nível é usado para registrar eventos de erro que afetam a operação de uma parte do sistema ou funcionalidade, mas não necessariamente o sistema como um todo. Erros que são capturados e gerenciados ainda podem ser logados neste nível.

### CRITICAL

* **Descrição**: O nível CRITICAL indica um erro grave que impede a continuação da execução do programa.
* **Uso**: É usado para erros que necessitam de atenção imediata, como um falha crítica no sistema que pode resultar em parada total do serviço ou aplicação. Este nível deve ser reservado para os problemas mais sérios.

### Como Utilizar

A seleção do nível de log adequado para diferentes mensagens permite que os desenvolvedores e administradores de sistema configurem os logs para capturar apenas as informações de que precisam. Por exemplo, em um ambiente de desenvolvimento, você pode querer ver todos os logs, desde DEBUG até CRITICAL, para entender completamente o comportamento da aplicação. Em contraste, em um ambiente de produção, você pode configurar para registrar apenas WARNING, ERROR, e CRITICAL, para reduzir o volume de dados gerados e se concentrar em problemas que necessitam de atenção.


#### Exemplo 4: Capturando Exceções com Log

Loguru também facilita o logging de exceções, capturando automaticamente informações de traceback.

```python
from loguru import logger

def minha_funcao():
    raise ValueError("Um erro aconteceu!")

try:
    minha_funcao()
except Exception:
    logger.exception("Uma exceção foi capturada")
```

Usando `logger.exception()`, Loguru automaticamente captura e loga o traceback da exceção, o que é extremamente útil para diagnóstico de erros.

Vamos criar um decorador utilizando o Loguru para adicionar automaticamente logs a qualquer função Python. Isso nos permite registrar automaticamente quando uma função é chamada e quando ela termina, junto com qualquer informação relevante, como argumentos da função e o resultado retornado (ou exceção lançada).

#### Exemplo 5: Capturando Exceções com Log

Agora, vamos ao código do decorador:

```python
from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper
```

Neste decorador, `log_decorator`, usamos `logger.info` para registrar quando a função decorada é chamada e o que ela retorna. Se uma exceção for lançada, usamos `logger.exception` para registrar a exceção, incluindo o traceback.

### Como Utilizar o Decorador

Agora, veja como aplicar o `log_decorator` a uma função:

```python
@log_decorator
def soma(a, b):
    return a + b

@log_decorator
def falha():
    raise ValueError("Um erro intencional")

# Testando as funções decoradas
soma(5, 3)  # Isso irá logar a chamada e o retorno
try:
    falha()  # Isso irá logar a chamada e a exceção
except ValueError:
    pass  # Ignora a exceção para fins de demonstração
```

Ao decorar as funções `soma` e `falha` com `@log_decorator`, automaticamente logamos a entrada e saída (ou exceção) dessas funções sem alterar o corpo delas. Isso é especialmente útil para debugar, monitorar a performance de aplicações ou simplesmente manter um registro de quais funções estão sendo chamadas e com quais argumentos.

### Benefícios do Uso de Decoradores com Loguru

O uso de decoradores em conjunto com o Loguru fornece uma abordagem elegante e poderosa para adicionar logs a aplicações Python. Sem a necessidade de modificar o corpo da função, podemos facilmente adicionar funcionalidades de logging, o que torna o código mais limpo, mantém a separação de preocupações e facilita a manutenção e o debugging.

Além disso, ao centralizar a lógica de logging no decorador, promovemos a reutilização de código e garantimos uma forma consistente de logar informações através de diferentes partes de uma aplicação.

### Conclusão

O Loguru oferece uma abordagem moderna e conveniente para logging em Python, simplificando muitos aspectos que requerem configuração manual detalhada com o módulo de logging padrão do Python. Seja para desenvolvimento, depuração ou produção, adicionar logging ao seu aplicativo com Loguru pode melhorar significativamente a visibilidade e a capacidade de diagnóstico do seu código.

### Desafio

![imagem_03](./pic/3.jpg)

Aplicar decorador de Log, Timer e Qualidade em nossa ETL

![imagem_03](./pic/pic_05.png)

