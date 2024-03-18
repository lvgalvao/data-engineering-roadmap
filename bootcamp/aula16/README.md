# Aula 16 - 18/03 - Revisão de Programação orientada a objetos

## Objetivo

- Revisão sobre o objetivo de trabalhar com POO
- Motivação para trabalharmos com Data Classes
- Motivação para trabalharmos com Pydantic
- Motivação para trabalharmos com ORM

## Abstração

**Definição:** Abstração, no contexto da programação orientada a objetos, é o processo de esconder os detalhes complexos de implementação e exibir apenas as funcionalidades essenciais de um objeto ou classe. Isso permite que pessoas do seu time trabalhem em um nível mais alto de abstração, focando no que o objeto faz, em vez de como ele faz.

**Exemplo em Python:**

```python
class Veiculo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def descrever(self):
        return f"Um {self.tipo} de cor {self.cor}"

# Usando a abstração
carro = Veiculo("carro", "azul")
print(carro.descrever())
```

Neste exemplo, a classe `Veiculo` abstrai as características e o comportamento de um veículo. O método `descrever` permite-nos obter uma descrição do veículo sem precisar saber detalhes específicos sobre sua implementação interna.

No Python, o método `__init__` e a palavra-chave `self` são fundamentais para a programação orientada a objetos (POO) e desempenham um papel crucial na definição e no trabalho com classes e objetos.

### O método `__init__`

* **Definição e Propósito:** O método `__init__` é um método especial, também conhecido como construtor, em classes Python. Ele é chamado automaticamente quando um novo objeto da classe é criado. O propósito principal do método `__init__` é inicializar os atributos do novo objeto, configurando-o com os valores iniciais necessários ou o estado padrão.
    
* **Sintaxe e Uso:** O método `__init__` é definido dentro de uma classe e pode aceitar argumentos além do `self` (que é obrigatório). Estes argumentos são usados para passar valores iniciais para o objeto.

```python
class Veiculo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
```

Neste exemplo, a classe `Veiculo` tem um método `__init__` que inicializa cada novo objeto `Veiculo` com `tipo` e `cor`.

### A palavra-chave `self`

* **Definição e Propósito:** `self` é uma referência à instância atual da classe e é usado para acessar variáveis e métodos associados a essa instância atual. Em outras palavras, `self` permite que um objeto acesse seus próprios atributos e métodos de dentro da classe.
    
* **Uso:** `self` é sempre o primeiro parâmetro dos métodos de uma classe, incluindo o método `__init__`. Não é uma palavra-chave reservada da linguagem Python, mas é uma convenção fortemente adotada. Poderíamos usar outra palavra, mas usar `self` é considerado uma boa prática e ajuda a manter o código legível e compreensível para outros desenvolvedores.
    

```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial  # `self.saldo` é um atributo da instância

    def depositar(self, quantia):
        self.saldo += quantia  # Acessa o atributo `saldo` da instância atual

    def sacar(self, quantia):
        if quantia <= self.saldo:  # Verifica o saldo da instância atual
            self.saldo -= quantia
```

* **Por que `self` é necessário?** Sem `self`, os métodos da classe não saberiam a qual instância (objeto) eles pertencem. `self` fornece uma maneira de acessar os atributos e métodos do objeto específico, permitindo que cada instância da classe tenha seu próprio estado e comportamento.

O método `__init__` e a palavra-chave `self` são essenciais para definir o comportamento e o estado inicial dos objetos em Python. Eles permitem que as classes sejam projetadas de forma flexível e reutilizável, mantendo o código organizado e claro. Entender esses conceitos é crucial para qualquer desenvolvedor que trabalhe com programação orientada a objetos em Python.

### Abstração de Processos

**Definição:** Abstração de processos refere-se à simplificação de um processo complexo, definindo um método ou função que encapsula esse processo. O usuário da classe ou função pode invocá-lo sem precisar entender os detalhes internos do processo.

**Exemplo em Python:**

```python
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            return True
        return False

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            return True
        return False

# Usando abstração de processos
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(20)
print(f"Saldo atual: {conta.saldo}")
```

Aqui, os métodos `depositar` e `sacar` encapsulam os processos de depósito e saque em uma conta bancária, escondendo os detalhes de implementação do usuário.

### Abstração de Dados

**Definição:** Abstração de dados é um conceito que envolve criar estruturas de dados que só expõem operações relevantes para o uso desses dados, escondendo detalhes específicos de implementação. Permite que os dados sejam manipulados através de interfaces definidas, garantindo uma manipulação segura e controlada.

**Exemplo em Python:**

```python
class Pilha:
    def __init__(self):
        self._elementos = []

    def empilhar(self, item):
        self._elementos.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self._elementos.pop()

    def esta_vazia(self):
        return len(self._elementos) == 0

# Usando abstração de dados
pilha = Pilha()
pilha.empilhar("Python")
pilha.empilhar("C++")
print(pilha.desempilhar())  # C++
print(pilha.desempilhar())  # Python
```

Neste exemplo, a classe `Pilha` é uma abstração de dados que permite ao usuário empilhar e desempilhar itens. A implementação interna (uma lista Python) é oculta do usuário, que interage com a pilha através de métodos claramente definidos.

A abstração e suas variantes (abstração de processos e abstração de dados) são fundamentais na orientação a objetos, pois permitem simplificar a complexidade, focando nas operações importantes e escondendo detalhes desnecessários. Isso facilita a compreensão, o uso e a manutenção do código.

Ao falar sobre abstração de dados no contexto da programação e, especificamente, no Python, é importante entender que essas abstrações são frequentemente referidas como "tipos de dados abstratos" (ADTs). Um tipo de dados abstrato é uma modelagem matemática para tipos de dados, onde um tipo de dados é definido pelo seu comportamento (semântica), do ponto de vista de um usuário dos dados, especificamente em termos de possíveis valores, possíveis operações sobre dados desse tipo, e o comportamento dessas operações.

### Tipos de Dados Abstratos no Python

Python, sendo uma linguagem de programação de alto nível, oferece várias abstrações de dados integradas, conhecidas como tipos de dados abstratos. Esses ADTs incluem, mas não se limitam a:

* **String:** São coleções de caracteres. São abstrações de palavras.

* **Listas:** São coleções ordenadas e mutáveis de itens. As listas são versáteis e podem conter itens de diferentes tipos, incluindo outras listas.
    
* **Tuplas:** Semelhantes às listas, mas imutáveis. Uma vez criadas, o conteúdo de uma tupla não pode ser alterado.
    
* **Dicionários:** São coleções não ordenadas de pares chave-valor. As chaves são únicas dentro de um dicionário, e os valores podem ser de qualquer tipo. Os dicionários são mutáveis, permitindo a modificação de dados.    

Cada um desses tipos encapsula um conjunto de operações específicas que podem ser realizadas com eles, além de gerenciar a memória e otimizar o desempenho. Por exemplo, os dicionários em Python são implementados como tabelas de hash, o que permite uma busca de tempo quase constante para inserir, buscar e deletar operações, tornando-os incrivelmente eficientes para certos tipos de operações.

### A Importância da Abstração de Dados

A abstração de dados e os ADTs no Python permitem que os desenvolvedores se concentrem na lógica de alto nível de seus programas, sem se preocupar com os detalhes de baixo nível de como os dados são armazenados e manipulados. Isso não apenas melhora a legibilidade e a manutenibilidade do código, mas também permite a reutilização de código e a criação de programas mais robustos e eficientes.

Por exemplo, ao usar um dicionário em Python, um desenvolvedor não precisa entender como uma tabela de hash é implementada ou como as colisões são tratadas. Em vez disso, o desenvolvedor pode se concentrar em como usar o dicionário para mapear chaves a valores de forma eficaz dentro de seu programa.

Em resumo, a abstração de dados e os tipos de dados abstratos são conceitos fundamentais em Python e na programação em geral, fornecendo uma poderosa ferramenta para os desenvolvedores organizarem e manipularem dados de forma eficiente e eficaz.

Os Tipos Abstratos de Dados (TADs) são uma parte fundamental do design e da implementação de software, oferecendo uma maneira de encapsular estruturas de dados e as operações que podem ser realizadas sobre elas. Eles são chamados de "abstratos" porque escondem os detalhes internos da implementação do usuário, permitindo que os dados sejam manipulados apenas através de um conjunto definido de operações. Esta abstração oferece várias vantagens significativas, incluindo confiabilidade, redução de código e redução de conflitos de nomes.

### Confiabilidade

Os TADs aumentam a confiabilidade do software ao garantir que os dados só possam ser manipulados de maneiras predefinidas e seguras. Por exemplo, se você tem uma pilha implementada como um tipo abstrato de dados, o usuário dessa pilha só pode adicionar ou remover itens de acordo com as regras da pilha (LIFO - Last In, First Out). Isso previne erros comuns, como tentativas de acessar elementos que não existem ou manipular os dados de maneiras inesperadas, o que poderia levar a bugs ou comportamento indefinido do programa.

### Redução de Código

Ao usar TADs, é possível reutilizar código de maneira eficiente. Uma vez que um TAD é implementado, ele pode ser usado em diferentes partes de um programa, ou até mesmo em diferentes projetos, sem a necessidade de reimplementar suas funcionalidades. Isso não apenas economiza tempo e esforço durante o desenvolvimento de software, mas também contribui para a manutenção do código, já que atualizações ou correções em um TAD se refletem automaticamente em todas as partes do programa que o utilizam.

## Glossário

Para entender melhor a programação orientada a objetos em Python, vamos explorar um glossário de alguns termos fundamentais, complementando cada definição com exemplos.

### Classe

**Definição:** Uma classe é uma abstração de dados que define um tipo de objeto, especificando os dados que ele pode conter e os métodos que pode executar. Em outras palavras, uma classe é como um "blueprint" ou modelo para criar instâncias (objetos) com características e comportamentos específicos.

**Exemplo em Python:**

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacao(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")
```

Neste exemplo, `Veiculo` é uma classe que tem atributos `marca` e `modelo`, além de um método `mostrar_informacao` para exibir essas informações.

### Atributos

**Definição:** Atributos são variáveis que pertencem a uma classe ou instância, representando as características ou propriedades do objeto. Eles são definidos dentro de uma classe e podem ser acessados e modificados por métodos da classe.

**Exemplo em Python:**

```python
# Usando a classe Veiculo definida anteriormente
meu_veiculo = Veiculo("Toyota", "Corolla")
print(meu_veiculo.marca)  # Atributo da instância
print(meu_veiculo.modelo) # Outro atributo da instância
```

Aqui, `marca` e `modelo` são atributos da instância `meu_veiculo` da classe `Veiculo`.

### Métodos

**Definição:** Métodos são funções definidas dentro de uma classe que descrevem os comportamentos ou ações que os objetos daquela classe podem executar. Eles são uma forma de abstração de processos, pois encapsulam o código que executa operações específicas.

**Exemplo em Python:**

```python
# Usando a classe Veiculo definida anteriormente
meu_veiculo = Veiculo("Ford", "Fusion")
meu_veiculo.mostrar_informacao()  # Chamada de método
```

`mostrar_informacao` é um método da classe `Veiculo` que exibe informações sobre uma instância específica.

### Instância

**Definição:** Uma instância é um objeto específico criado a partir de uma classe. Cada instância tem seus próprios atributos, que podem ser definidos como valores distintos, independentes de outras instâncias da mesma classe.

**Exemplo em Python:**

```python
carro1 = Veiculo("Honda", "Civic")  # Cria uma instância da classe Veiculo
carro2 = Veiculo("Tesla", "Model S") # Cria outra instância da classe Veiculo
```

Aqui, `carro1` e `carro2` são instâncias da classe `Veiculo`, cada uma com seus próprios atributos `marca` e `modelo`.

Este glossário cobre alguns dos conceitos mais importantes da programação orientada a objetos em Python, fornecendo uma base sólida para entender como classes, atributos, métodos e instâncias são usados para modelar dados e comportamentos no mundo real.