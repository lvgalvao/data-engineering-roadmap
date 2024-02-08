# Aula 02 - Ambientes Virtuais e Gerenciamento de Pacotes em Python

Revisão para quem não conseguiu

## Objetivos

* Compreender a importância dos ambientes virtuais para o desenvolvimento em Python.
* Aprender a criar e gerenciar ambientes virtuais utilizando `pip`, `pipx`, `venv` e `poetry`.
* Explorar as vantagens e casos de uso de cada ferramenta.

## Pré-requisitos

* Python e VSCode previamente instalados.
* Conhecimento básico sobre a instalação de pacotes em Python.

## Agenda

1. Introdução (5 minutos)
2. Ambientes Virtuais com `venv` (15 minutos)
3. Gerenciamento de Pacotes com `pip` (15 minutos)
4. Isolamento de Pacotes com `pipx` (15 minutos)
5. Gerenciamento de Dependências com `poetry` (15 minutos)
6. Conclusão e Exercício Prático (10 minutos)

## 1. Introdução (5 minutos)

Nesta aula, vamos explorar a importância dos ambientes virtuais e como eles podem nos ajudar a manter nossos projetos Python organizados e isolados.

## 2. Ambientes Virtuais com `venv` (15 minutos)

O `venv` é uma ferramenta integrada ao Python que permite criar ambientes virtuais facilmente.

* Criar um novo ambiente virtual:
    
    ```
    python -m venv nome_do_ambiente
    ```
    
* Ativar o ambiente virtual:
    * No Windows:
        
        ```
        nome_do_ambiente\Scripts\activate
        ```
        
    * No macOS e Linux:
        
        ```bash
        source nome_do_ambiente/bin/activate
        ```
        

## 3. Gerenciamento de Pacotes com `pip` (15 minutos)

O `pip` é o gerenciador de pacotes padrão do Python, usado para instalar e gerenciar pacotes.

* Instalar um pacote:
    
    ```bash
    pip install nome_do_pacote
    ```
    
* Desinstalar um pacote:
    
    ```bash
    pip uninstall nome_do_pacote
    ```

* Mostrar informações sobre um pacote:
    
    ```bash
    pip show nome_do_pacote
    ```

* Listar pacotes instalados:
    
    ```bash
    pip list
    ```
    
* Criar um arquivo de requisitos:
    
    ```bash
    pip freeze > requirements.txt
    ```

## 4. Isolamento de Pacotes com `pipx` (15 minutos)

O `pipx` é uma ferramenta que permite instalar pacotes Python em ambientes virtuais isolados, facilitando a gestão de pacotes executáveis.

* Instalar um pacote globalmente:
    
    ```
    pipx install nome_do_pacote
    ```
    
* Executar um pacote instalado via `pipx`:
    
    ```
    nome_do_pacote
    ```
    

## 5. Gerenciamento de Dependências com `poetry` (15 minutos)

O `poetry` é uma ferramenta de gerenciamento de dependências Python que visa simplificar e unificar o trabalho com projetos Python.

* Criar um novo projeto:
    
    ```arduino
    poetry new nome_do_projeto
    ```
    
* Adicionar uma dependência:
    
    ```csharp
    poetry add nome_do_pacote
    ```
    
* Instalar dependências do projeto:
    
    ```
    poetry install
    ```
    

## 6. Conclusão e Exercício Prático (10 minutos)

Parabéns! Agora você conhece diferentes maneiras de criar e gerenciar ambientes virtuais e pacotes em Python. Para praticar, proponho o seguinte exercício:

* Crie um novo ambiente virtual utilizando `venv`.
* Ative o ambiente virtual e instale o pacote `requests` utilizando `pip`.
* Instale o `httpie` globalmente utilizando `pipx`.
* Crie um novo projeto com `poetry` e adicione o pacote `numpy` como dependência.
* Experimente importar os pacotes instalados em seus scripts Python e execute-os para verificar se estão funcionando corretamente.

## Recursos Adicionais

* Documentação `venv`
* Documentação `pip`
* Documentação `pipx`
* Documentação `poetry`

## Conclusão

Nesta aula, exploramos diferentes ferramentas para criar e gerenciar ambientes virtuais e pacotes em Python. Essas habilidades são essenciais para manter nossos projetos organizados e facilitar a colaboração com outros desenvolvedores. Continue praticando e explorando as ferramentas apresentadas para se tornar um programador Python mais eficiente e produtivo! Nos vemos na próxima aula!

## Portfolio 02 e Exercício Prático (30 minutos)

Parabéns por dominar as ferramentas de gerenciamento de ambientes virtuais e pacotes em Python! Agora, vamos avançar um pouco mais com um exercício prático desafiador:

### Exercício Prático: Construção de uma Calculadora Simples

Neste exercício, vamos criar uma calculadora simples em Python utilizando os pacotes `requests`, `httpie` e `pandas`. Siga os passos abaixo:

1. **Crie um novo ambiente virtual utilizando `venv`:**
    
    * Utilize o comando `python -m venv calculadora_venv` para criar um novo ambiente virtual chamado `calculadora_venv`.
2. **Ative o ambiente virtual e instale o pacote `requests` utilizando `pip`:**
    
    * Ative o ambiente virtual:
        * No Windows: `calculadora_venv\Scripts\activate`
        * No macOS/Linux: `source calculadora_venv/bin/activate`
    * Instale o pacote `requests` utilizando o comando `pip install requests`.
3. **Instale o `httpie` globalmente utilizando `pipx`:**
    
    * Utilize o comando `pipx install httpie` para instalar o `httpie` globalmente.
4. **Crie um novo projeto com `poetry` e adicione o pacote `pandas` como dependência:**
    
    * Crie um novo projeto com `poetry` utilizando o comando `poetry new calculadora_projeto`.
    * Navegue até o diretório do projeto (`calculadora_projeto`) e adicione o pacote `pandas` como dependência com o comando `poetry add pandas`.
5. **Construa a calculadora:**
    
    * Crie um arquivo Python chamado `calculadora.py` no diretório do projeto.
    * Utilize os pacotes instalados para realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão.
    * Utilize o `requests` ou o `httpie` para realizar uma solicitação HTTP para uma API externa que forneça operações matemáticas mais complexas, como exponenciação, raiz quadrada, etc.
6. **Teste sua calculadora:**
    
    * Experimente importar os pacotes instalados em seus scripts Python e execute-os para verificar se estão funcionando corretamente.
    * Teste diferentes operações matemáticas para garantir que sua calculadora esteja funcionando como esperado.

Este exercício prático permitirá que você aplique seus conhecimentos sobre o uso de ambientes virtuais, gerenciamento de pacotes e realização de solicitações HTTP em Python para construir uma aplicação real. Divirta-se e bons estudos!