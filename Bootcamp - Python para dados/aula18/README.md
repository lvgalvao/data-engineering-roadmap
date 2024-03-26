# Aula 18: API - Conjunto de ferramentas para manipular SQL em 

![imagem_01](./pics/1.jpg)

Bem-vindo à décima oitava aula do bootcamp!

# O que é uma API?

Uma API (Application Programming  Interface) é um conjunto de rotinas e padrões (contratos) estabelecidos por uma aplicação, para que outras aplicações possam utilizar as funcionalidades dessa aplicação.

![Imagem](assets/server-server.png)

# Por que usar uma API?

Nos últimos anos, a Internet se transformou de uma rede de servidores web que serviam principalmente páginas estáticas para navegadores de internet...

![Internet](https://thefloppydisk.files.wordpress.com/2013/05/web10.png?w=1248)

...em uma arquitetura cliente-servidor, onde aplicativos web e mobile se comunicam com diferentes aplicações, cada vez mais por meio de APIs RESTful simples, mas poderosas.

![Imagem](https://thefloppydisk.files.wordpress.com/2013/05/web20.png?w=1245)

# As regras do jogo

Basicamente uma API é um contrato que define como uma aplicação vai se comunicar com a outra. Como os dados serão enviados e recebidos.

![Contrato](pics/contract.png)

# O que é uma API REST?

REST é um acrônimo para REpresentational STATE Transfer, que é um estilo de arquitetura para sistemas distribuídos.

![Rest](pics/apirest.png)

# Como se comunicar com ela?

- Nosso protocolo (ex: https)

- Nosso servidor tem um endereço (ex: pokeapi.co)

- Nosso servidor tem uma porta (ex: 8080 para http e 443 para https)

- E precisamos acessar um recurso ou como constumamos chamar, endpoint ou rota (ex: /api/character)

``` 
https://pokeapi.co/api/v2/pokemon/15
```

# Nossos verbos

O protocolo HTTP é a base usada por trás das APIs REST e as "requisita" utilizando diversos "tipos". Os mais comuns são:

## O que é o CRUD? 

Create, Read, Update e Delete

- POST: (Create) Criar um recurso
- GET: (Read) Obter um recurso
- PUT: (Update) Atualizar um recurso
- DELETE: Remover um recurso

# Qual a diferença entre REST e RESTful?

REST é um estilo de arquitetura para sistemas distribuídos, enquanto RESTful é a implementação desse estilo.

# Vamos para a prática?

Vamos usar o VScode e o terminal para conectar e salvar os dados de uma API em um banco de dados.