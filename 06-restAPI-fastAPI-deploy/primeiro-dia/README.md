## Objetivo

## README em revisão

Excalidraw: https://link.excalidraw.com/l/8pvW6zbNUnD/7APGEyy8COJ

Este workshop visa introduzir os conceitos fundamentais (Redes, protocolo, HTTP, comumicação entre processos etc) e as práticas necessárias para criar uma API usando a framework FastAPI em Python.

Os participantes aprenderão desde a configuração do ambiente de desenvolvimento até a criação e documentação de APIs.

## Curl (Cliente por linha de comando)

### Introdução ao Curl

**Curl** (Client URL) é uma ferramenta de software e uma biblioteca de linha de comando usada para transferir dados com URLs. Ela suporta uma diversidade de protocolos, como HTTP, HTTPS, FTP, FTPS, SCP, SFTP, entre outros. Amplamente utilizada por desenvolvedores e administradores de sistema, a ferramenta permite a interação com servidores web e outros tipos de servidores de internet para baixar ou enviar dados.

### Por Que Usar Curl?

**1. Versatilidade:** Curl pode ser usado para testar conectividade de API, desenvolver e depurar serviços web, automatizar tarefas de upload e download de arquivos e muito mais.

**2. Suporte Amplo de Protocolos:** Suportando uma grande variedade de protocolos de comunicação de dados, curl é extremamente flexível para qualquer necessidade de rede.

**3. Automação:** Curl é ideal para scripts automatizados devido à sua natureza de linha de comando. Ele pode ser integrado em scripts bash ou shell para automação de tarefas de rede.

**4. Disponibilidade:** Disponível em quase todas as plataformas Unix-like, incluindo Linux e macOS, e também em Windows, curl é uma ferramenta universal.

**5. Comunidade e Suporte:** Sendo um projeto de código aberto, curl é bem documentado e tem uma comunidade ativa que contribui para sua melhoria contínua.

### O Que é o Protocolo HTTP?

**HTTP (HyperText Transfer Protocol)** é o protocolo de comunicação utilizado para transmitir informações na web. É a base para qualquer troca de dados na internet, permitindo a comunicação entre clientes web (navegadores) e servidores web. O protocolo define métodos de requisição que indicam a ação desejada para um determinado recurso, como `GET` para solicitar dados de um recurso, ou `POST` para submeter dados para serem processados a um recurso.

### Características do HTTP:

**1. Simples e Extensível:** Projetado para ser simples e fácil de implementar, enquanto permite extensões para aumentar sua funcionalidade.

**2. Stateless:** HTTP é um protocolo sem estado, o que significa que cada requisição é independente das outras e não deve afetar o comportamento das outras requisições. Contudo, sessões e cookies podem ser usados para adicionar estado em comunicações HTTP.

**3. Flexível:** HTTP permite a transferência de qualquer tipo de dados, desde que ambas as partes (cliente e servidor) possam interpretar esses dados.

Aqui estão os oito exercícios propostos para praticar o uso do `curl`, acompanhados das respostas esperadas para cada um:

### Exercício 1: Fazendo Requisições Básicas

**Objetivo**: Familiarizar-se com requisições GET e a saída do `curl`.

* **Comando**:
    
    ```bash
    curl -v http://httpbin.org/get
    ```
    
* **Resposta Esperada**: Você verá detalhes completos da requisição e da resposta, incluindo cabeçalhos HTTP enviados e recebidos. Isso inclui informações sobre o método usado (GET), o host acessado, e cabeçalhos como `User-Agent` e `Accept`.

### Exercício 2: Trabalhando com Parâmetros de Query

**Objetivo**: Aprender a enviar parâmetros de query em URLs.

* **Comando**:
    
    ```bash
    curl http://httpbin.org/get?name=John&age=30
    ```
    
* **Resposta Esperada**: A resposta de httpbin.org refletirá os parâmetros que você enviou. No JSON de resposta, você verá um objeto "args" contendo `"name": "John", "age": "30"`.

### Exercício 3: Postando Dados JSON

**Objetivo**: Praticar o envio de dados JSON em uma requisição POST.

* **Comando**:
    
    ```bash
    curl -X POST http://httpbin.org/post -H "Content-Type: application/json" -d '{"username":"john", "password":"12345"}'
    ```

Importância do -X:
O uso do -X é particularmente importante quando você precisa realizar operações específicas que requerem diferentes tipos de métodos HTTP. Por exemplo:

GET: Usado para solicitar dados de um recurso específico.
POST: Usado para enviar dados para serem processados para um recurso específico. Normalmente resulta em uma mudança de estado ou efeitos colaterais no servidor.
PUT: Usado para enviar dados para atualizar um recurso existente.
DELETE: Usado para deletar um recurso específico.
    
* **Resposta Esperada**: Httpbin irá ecoar de volta os dados que você enviou em um objeto JSON. A seção `json` da resposta incluirá os dados `{"username": "john", "password": "12345"}`.

### Exercício 4: Usando Diferentes Métodos HTTP

**Objetivo**: Experimentar com diferentes métodos HTTP, como POST, DELETE, PUT.

* **Comando PUT**:
    
    ```bash
    curl -X PUT http://httpbin.org/put -d "data=example"
    ```
    
* **Comando DELETE**:
    
    ```bash
    curl -X DELETE http://httpbin.org/delete
    ```
    
* **Resposta Esperada**: Para PUT, httpbin mostrará os dados que você enviou no corpo da requisição, enquanto para DELETE, você receberá uma confirmação de que a requisição DELETE foi recebida, geralmente sem corpo de dados.

### Exercício 5: Manipulando Headers

**Objetivo**: Aprender a enviar cabeçalhos customizados.

* **Comando**:
    
    ```bash
    curl http://httpbin.org/headers -H "X-My-Custom-Header: 12345"
    ```
    
* **Resposta Esperada**: A resposta incluirá um objeto `headers` que mostra todos os cabeçalhos recebidos, incluindo seu cabeçalho personalizado `X-My-Custom-Header` com o valor `12345`.

### Exercício 6: Trabalhando com Cookies

**Objetivo**: Entender como enviar e receber cookies.

* **Comando**:
    
    ```bash
    curl http://httpbin.org/cookies/set?name=value
    curl http://httpbin.org/cookies
    ```
    
* **Resposta Esperada**: Após definir o cookie, a segunda requisição mostrará um objeto `cookies` com o par `{"name": "value"}`.

### Exercício 7: Baixando e Salvando Arquivos

**Objetivo**: Praticar o download de arquivos usando `curl`.

* **Comando**:
    
    ```bash
    curl https://via.placeholder.com/150 -o example.jpg
    ```
    
* **Resposta Esperada**: O arquivo de imagem será baixado e salvo localmente com o nome `example.jpg`. Você não verá saída no terminal, exceto mensagens relacionadas ao progresso do download.

### Exercício 8: Explorando APIs Restritas

**Objetivo**: Aprender a lidar com autenticação.

* **Comando**:
    
    ```bash
    curl -u user:passwd https://httpbin.org/basic-auth/user/passwd
    ```
    
* **Resposta Esperada**: Se a autenticação for bem-sucedida, httpbin retornará um status de sucesso e confirmará que você foi autenticado. 

## Programação

### 1. Introdução a APIs e Web Servers

* **O que é uma API?**
    * Explicação de API (Interface de Programação de Aplicações) como um conjunto de regras e especificações que softwares podem seguir para se comunicar.

* **Diferenças entre API e Web Server**
    * Clarificação de que um Web Server lida com requisições HTTP para servir conteúdo web, enquanto uma API fornece uma interface para realizar operações específicas através de um servidor.

### 2. Introdução ao FastAPI

* **Visão Geral do FastAPI**
    * Discussão sobre as características do FastAPI, como alta performance, fácil aprendizado e recursos como a geração automática de documentação.
* **Comparação com Outras Frameworks**
    * Breve comparação do FastAPI com outras frameworks populares como Flask e Django, destacando a facilidade de uso e eficiência em operações assíncronas.

### 3. Configuração do Ambiente de Desenvolvimento

* **Instalação do Python e Setup do Ambiente**
    * Passo a passo para configurar o ambiente Python, incluindo a instalação do FastAPI e do servidor Uvicorn usando pip.

### 4. Criando sua Primeira API com FastAPI

* **Hello World API**
    * Tutorial para criar um endpoint básico que retorna uma mensagem de "Hello, World!" usando FastAPI.

```python
from fastapi import FastAPI

app = FastAPI()

# Decorator -> É aqui que faz a mágica de transformar nossa função.
@app.get("/")
# Function é função padrão do Python
def root(): # O nome não importa
    return {"message": "Hello world!"} # Essa será a data que vamos retornar ao usuário
```

```bash
uvicorn main:app
```

```bash
uvicorn main:app --reload
```

HTTP metodos

#### Curl

Para usar `curl` para fazer uma requisição à sua API que está rodando com FastAPI, você pode enviar dados como JSON através de uma requisição POST. Suponhamos que você tenha um endpoint em sua API que espera receber os dados de uma casa e então retorna uma previsão de preço baseada nessas informações. Aqui está como você pode fazer isso com `curl`.

### Exemplo de Requisição com Curl

Suponha que seu endpoint para prever o preço da casa esteja configurado como `http://127.0.0.1:8000/prever/` e aceite um JSON com dois campos: `tamanho` e `quartos`. Aqui está como você pode enviar uma requisição:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/prever/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tamanho": 120,
  "quartos": 3
}'
```

### Explicação do Comando Curl

* `-X 'POST'`: Especifica o método HTTP para a requisição, que é POST neste caso.
* `http://127.0.0.1:8000/prever/`: URL do endpoint da API.
* `-H 'accept: application/json'`: Define o cabeçalho HTTP para indicar que a resposta esperada deve ser em JSON.
* `-H 'Content-Type: application/json'`: Define o cabeçalho HTTP para indicar que o corpo da requisição está em formato JSON.
* `-d '{...}'`: Os dados sendo enviados à API. Substitua os valores de `tamanho` e `quartos` conforme necessário para os dados específicos da casa que você quer avaliar.

### Testando a Requisição

1. Certifique-se de que sua API FastAPI esteja rodando e acessível em `http://127.0.0.1:8000`.
2. Abra um terminal e execute o comando `curl` fornecido.
3. Observe a resposta da API, que deve incluir a previsão do preço da casa baseada nos dados fornecidos.

Usar os cabeçalhos Accept e Content-Type nas suas requisições HTTP é uma forma de comunicar claramente ao servidor tanto o formato dos dados que você está enviando quanto o formato que você espera receber em resposta:

Content-Type: application/json: Este cabeçalho informa ao servidor que o corpo da requisição que você está enviando está em formato JSON. É uma maneira de dizer, "Ei, os dados que estou enviando estão em JSON; por favor, interprete-os dessa forma."
Accept: application/json: Este cabeçalho diz ao servidor que você deseja que a resposta seja em JSON. Isso é particularmente útil em APIs que podem retornar dados em diferentes formatos. Ao especificar application/json, você está solicitando que a API responda com dados nesse formato específico.

#### Postman

Também temos a opção usar o Postman (uma aplicação)


### 5. Trabalhando com Dados

* **Uso de Modelos Pydantic**
    * Introdução aos modelos Pydantic para validação de dados e como integrá-los com FastAPI.
* **Endpoints GET e POST**
    * Criação de exemplos práticos de endpoints que lidam com métodos GET e POST para enviar e receber dados.

### 6. Uvicorn: O Servidor ASGI

* **Por que Uvicorn?**
    * Explicação sobre o papel do Uvicorn como um servidor ASGI, necessário para executar aplicações FastAPI de forma eficiente e assíncrona.

### 7. Documentação Automática

* **Swagger UI**
    * Demonstração de como acessar e utilizar a documentação automática gerada pelo FastAPI.

### 8. Exercícios Práticos

* **Hands-on Coding**
    * Série de exercícios práticos para aplicar o conhecimento adquirido na criação de APIs mais complexas.
* **Desafio com Banco de Dados**
    * Desafio para criar uma API que interage com um banco de dados usando operações básicas de CRUD.

### 9. Sessão de Perguntas e Respostas (Q&A)

* **Discussão Aberta**
    * Espaço para perguntas, troca de ideias e esclarecimento de dúvidas.

### 10. Encerramento

* **Recursos para Aprendizado Contínuo**
    * Compartilhamento de recursos adicionais, como documentação online, tutoriais e fóruns para aprofundamento nos temas abordados.

## Materiais Necessários

* Slides das apresentações.
* Códigos de exemplo e templates para exercícios.
* Acesso à Internet para documentação e pesquisa.

## Pré-requisitos

* Conhecimento básico de programação em Python.
* Ambiente de desenvolvimento Python configurado com acesso à internet.

## Recursos Adicionais

* Documentação Oficial do FastAPI
* Pydantic Documentation
* [Uvicorn Documentation](https://www.uvicorn.org/)


## Ideias