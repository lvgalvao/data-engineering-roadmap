**Aula de 3 Horas: Construindo um Projeto ETL com Python e Scrapy**

---

**Objetivo da Aula:**

- Desenvolver um pipeline ETL completo que coleta dados do Mercado Livre utilizando Scrapy.
- Ensinar passo a passo desde a instalação das ferramentas até a implementação completa do projeto.
- Proporcionar experiência prática em web scraping, processamento e armazenamento de dados usando Python.

---

**Estrutura da Aula:**

### **1ª Hora: Introdução e Preparação do Ambiente**

**1.1 Introdução ao Projeto**

- Conceito de ETL (Extract, Transform, Load).
- Visão geral sobre o Scrapy e suas vantagens.
- Objetivos específicos do projeto:
  - Coletar dados de produtos do Mercado Livre.
  - Processar e armazenar os dados coletados.

**1.2 Preparação do Ambiente**

- **Instalação do Python**
  - Verificação da versão instalada.
  - Links para download caso não esteja instalado.
- **Criação de Ambiente Virtual**
  - Uso do `venv` para isolamento de dependências.
  - Ativação do ambiente virtual.
- **Instalação do Scrapy**
  - Comandos para instalação via `pip`.
  - Verificação da instalação.

**1.3 Configuração do Projeto**

- **Inicialização do Projeto Scrapy**
  - Comando `startproject` e sua estrutura.
- **Exploração da Estrutura de Pastas**
  - Explicação dos principais arquivos e pastas:
    - `scrapy.cfg`
    - Diretório do projeto
    - Diretório `spiders`

---

### **2ª Hora: Desenvolvimento do Spider para o Mercado Livre**

**2.1 Análise do Site do Mercado Livre**

- **Entendendo a Estrutura do Site**
  - Identificação das URLs iniciais.
  - Uso do Inspetor de Elementos do navegador para encontrar seletores CSS ou XPath.

**2.2 Criação do Spider**

- **Gerando um Novo Spider**
  - Comando `genspider` e suas opções.
- **Definição das Configurações Básicas**
  - Nome do spider.
  - Domínios permitidos.
  - URLs de início (`start_urls`).

**2.3 Implementação dos Métodos de Extração**

- **Método `parse`**
  - Extração de dados desejados (título, preço, link, etc.).
- **Tratamento de Paginação**
  - Identificação do link para a próxima página.
  - Implementação da navegação entre páginas.

---

### **3ª Hora: Processamento e Armazenamento dos Dados**

**3.1 Processamento dos Dados**

- **Uso de Pipelines do Scrapy**
  - Criação de um pipeline para limpeza de dados.
  - Ativação do pipeline no arquivo `settings.py`.

**3.2 Armazenamento em Banco de Dados**

- **Configuração do Banco de Dados**
  - Escolha entre SQLite ou PostgreSQL (para fins educacionais, SQLite é mais simples).
  - Instalação das bibliotecas necessárias (`sqlite3` ou `psycopg2`).

- **Integração com o Scrapy**
  - Modificação do pipeline para inserir dados no banco de dados.
  - Criação de tabelas e gerenciamento de conexões.

**3.3 Execução e Testes Finais**

- **Rodando o Spider**
  - Comando para executar o spider.
  - Verificação dos dados no banco de dados.
- **Depuração e Solução de Problemas**
  - Análise de erros comuns.
  - Boas práticas para evitar bloqueios e captchas.

**3.4 Encerramento da Aula**

- **Recapitulando o Aprendido**
  - Revisão dos principais pontos.
- **Dicas e Melhores Práticas**
  - Ética no web scraping.
  - Respeito ao arquivo `robots.txt`.
- **Próximos Passos**
  - Como expandir o projeto.
  - Integração com outras ferramentas (visualização de dados, por exemplo).

---

## **README.md**

```markdown
# Projeto ETL com Python e Scrapy - Coleta de Dados do Mercado Livre

Este projeto demonstra como construir um pipeline ETL utilizando Python e Scrapy para coletar dados do Mercado Livre, processá-los e armazená-los em um banco de dados SQL.

## **Índice**

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Inicialização do Projeto Scrapy](#inicialização-do-projeto-scrapy)
- [Criação do Spider para o Mercado Livre](#criação-do-spider-para-o-mercado-livre)
- [Execução do Spider](#execução-do-spider)
- [Processamento e Armazenamento dos Dados](#processamento-e-armazenamento-dos-dados)
- [Recursos Adicionais](#recursos-adicionais)

---

## **Pré-requisitos**

- **Python 3.6+**
- **Pip** (gerenciador de pacotes do Python)
- **Virtualenv** (opcional, mas recomendado)
- **Bibliotecas Python:**
  - Scrapy

## **Instalação**

### **1. Instale o Python**

Verifique se o Python está instalado:

```bash
python --version
```

Se não estiver instalado, faça o download e instale a partir do [site oficial do Python](https://www.python.org/downloads/).

### **2. Crie um Ambiente Virtual**

É recomendado usar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **Linux/MacOS:**

  ```bash
  source venv/bin/activate
  ```

### **3. Instale o Scrapy**

Com o ambiente virtual ativado, instale o Scrapy usando o pip:

```bash
pip install scrapy
```

Verifique se a instalação foi bem-sucedida:

```bash
scrapy --version
```

---

## **Inicialização do Projeto Scrapy**

Dentro do diretório do seu projeto, inicialize um novo projeto Scrapy:

```bash
scrapy startproject mercado_livre
```

Isso criará a seguinte estrutura de diretórios:

```
mercado_livre/
    scrapy.cfg
    mercado_livre/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```

---

## **Criação do Spider para o Mercado Livre**

Navegue até o diretório `mercado_livre/spiders`:

```bash
cd mercado_livre/mercado_livre/spiders
```

Crie um novo Spider chamado `mercado_spider`:

```bash
scrapy genspider mercado_spider mercadolivre.com.br
```

### **Editar o Spider**

Abra o arquivo `mercado_spider.py` e edite-o conforme necessário.

**Exemplo de código:**

```python
import scrapy

class MercadoSpider(scrapy.Spider):
    name = 'mercado_spider'
    allowed_domains = ['mercadolivre.com.br']
    start_urls = ['https://lista.mercadolivre.com.br/livros#D[A:livros]']

    def parse(self, response):
        for product in response.css('li.ui-search-layout__item'):
            yield {
                'titulo': product.css('h2.ui-search-item__title::text').get(),
                'preco': product.css('span.price-tag-fraction::text').get(),
                'link': product.css('a.ui-search-link::attr(href)').get(),
            }

        next_page = response.css('a.andes-pagination__link--next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

**Notas:**

- Certifique-se de que os seletores CSS correspondam à estrutura atual do site do Mercado Livre.
- A estrutura do site pode mudar, portanto, verifique os elementos usando o inspetor do navegador.

---

## **Execução do Spider**

Para executar o spider e salvar os dados coletados em um arquivo JSON:

```bash
scrapy crawl mercado_spider -o produtos.json
```

---

## **Processamento e Armazenamento dos Dados**

### **1. Configurar o Pipeline**

Abra o arquivo `pipelines.py` e edite-o para processar e armazenar os dados.

**Exemplo de código:**

```python
import sqlite3

class MercadoLivrePipeline:

    def open_spider(self, spider):
        self.connection = sqlite3.connect('mercado_livre.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                titulo TEXT,
                preco TEXT,
                link TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO produtos (titulo, preco, link) VALUES (?, ?, ?)
        ''', (
            item.get('titulo'),
            item.get('preco'),
            item.get('link')
        ))
        self.connection.commit()
        return item
```

### **2. Ativar o Pipeline**

No arquivo `settings.py`, ative o pipeline:

```python
ITEM_PIPELINES = {
    'mercado_livre.pipelines.MercadoLivrePipeline': 300,
}
```

---

## **Recursos Adicionais**

- [Documentação Oficial do Scrapy](https://docs.scrapy.org/en/latest/)
- [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Seletores CSS](https://www.w3schools.com/cssref/css_selectors.asp)
- [Uso de XPath no Scrapy](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpath)

---

## **Observações Finais**

- Certifique-se de respeitar os termos de uso do site do Mercado Livre.
- Evite sobrecarregar o servidor com muitas requisições simultâneas.
- Use `DOWNLOAD_DELAY` no `settings.py` para adicionar um atraso entre as requisições:

```python
DOWNLOAD_DELAY = 1  # atraso de 1 segundo
```