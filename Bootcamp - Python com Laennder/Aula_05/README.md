# Projeto ETL com Python e Scrapy - Coleta de Dados do Mercado Livre

Este projeto demonstra como construir um pipeline ETL utilizando Python e Scrapy para coletar dados do Mercado Livre, processá-los e armazená-los em um banco de dados SQL.

## **Índice**

- [Projeto ETL com Python e Scrapy - Coleta de Dados do Mercado Livre](#projeto-etl-com-python-e-scrapy---coleta-de-dados-do-mercado-livre)
  - [**Índice**](#índice)
  - [**Pré-requisitos**](#pré-requisitos)
  - [**Instalação**](#instalação)
    - [**1. Instale o Python**](#1-instale-o-python)
    - [**2. Crie um Ambiente Virtual**](#2-crie-um-ambiente-virtual)
    - [**3. Instale o Scrapy**](#3-instale-o-scrapy)
  - [**Inicialização do Projeto Scrapy**](#inicialização-do-projeto-scrapy)
  - [**Criação do Spider para o Mercado Livre**](#criação-do-spider-para-o-mercado-livre)
    - [**Editar o Spider**](#editar-o-spider)
  - [**Execução do Spider**](#execução-do-spider)
  - [**Processamento e Armazenamento dos Dados**](#processamento-e-armazenamento-dos-dados)
    - [**1. Configurar o Pipeline**](#1-configurar-o-pipeline)
    - [**2. Ativar o Pipeline**](#2-ativar-o-pipeline)
  - [**Recursos Adicionais**](#recursos-adicionais)
  - [**Observações Finais**](#observações-finais)

---

## **Pré-requisitos**

- **Python 3.12+**
- **Pip** (gerenciador de pacotes do Python)
- **Bibliotecas Python:**
  - Scrapy
  - Pandas
  - Streaming

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