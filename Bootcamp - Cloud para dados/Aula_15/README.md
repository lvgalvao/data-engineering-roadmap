# Aula 15: Construção de uma Página de Sorteio com AWS

## **Objetivo da Aula**

Nesta aula, vamos construir uma página de sorteio automática usando AWS. O usuário poderá inserir o nome do sorteio, o número mínimo e o número máximo, e nossa aplicação, utilizando AWS Lambda, retornará um número aleatório dentro desse intervalo. Vamos dividir o projeto em duas etapas principais, utilizando o AWS Amplify para hospedar a página e AWS Lambda para a lógica de geração do número.

## **Conteúdo**
1. Estruturação da aplicação.
2. Criando a página web com Amplify (Etapa 1 e Etapa 2).
3. Configuração da lógica de sorteio com Lambda.
4. Integração com API Gateway.
5. Persistindo dados com DynamoDB (opcional).
6. Controle de permissões com IAM.
7. Conclusão e boas práticas.

---

## **1. Estruturação da Aplicação**

Vamos criar uma aplicação simples, onde os usuários poderão realizar sorteios online. A página web será criada em duas etapas: a primeira será bem básica, e na segunda, vamos melhorar a interação e adicionar a funcionalidade de sorteio.

Os dados que o usuário fornecerá serão:
- Nome do sorteio
- Número mínimo
- Número máximo

Com essas informações, uma função Lambda será acionada para gerar um número aleatório entre os números fornecidos.

---

## **2. Criando a Página Web com Amplify**

### **O que é o Amplify?**
O AWS Amplify é uma ferramenta que facilita a criação e hospedagem de páginas web. Vamos utilizá-lo para hospedar nossa página de sorteio.

### **Etapa 1: Página Simples**

Nesta primeira etapa, vamos criar uma página estática simples com HTML, para garantir que a estrutura está funcionando corretamente.

#### **Passo a Passo: Criando a página HTML simples**

1. Crie um arquivo `index.html` com o seguinte conteúdo:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Sorteio Automático</title>
   </head>
   <body>
       <h1>Essa é nossa página de sorteio</h1>
       <p>Agora os nossos sorteios vão ficar automáticos!</p>
   </body>
   </html>
   ```

2. **Empacotamento e Upload para o Amplify:**
   - Comprima o arquivo `index.html` em um arquivo `.zip`.
   - No console da AWS, vá até **AWS Amplify** e crie um novo aplicativo.
   - Selecione a opção de **"Host a web app"**.
   - Faça o upload do arquivo `.zip` e implante o aplicativo.

Agora você tem uma página web simples com a estrutura inicial do seu projeto de sorteio.

---

## **3. Configurando a Lógica de Sorteio com Lambda**

### **O que é o Lambda?**
O AWS Lambda permite executar código em resposta a eventos. Vamos usá-lo para gerar um número aleatório entre o número mínimo e o máximo fornecido pelo usuário.

#### **Passo a Passo: Criando a Função Lambda**

1. No console da AWS, acesse **AWS Lambda** e crie uma nova função chamada `SorteioFunction`.
2. Selecione **Python 3.9** como a linguagem de execução.
3. Substitua o código padrão pelo seguinte:

```python
import json
import random

def lambda_handler(event, context):
    nome_sorteio = event['nomeSorteio']
    num_min = int(event['numMin'])
    num_max = int(event['numMax'])
    numero_sorteado = random.randint(num_min, num_max)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'nomeSorteio': nome_sorteio,
            'numeroSorteado': numero_sorteado
        })
    }
```

Aqui está um body em JSON para testar essa função Lambda:

```json
{
    "nomeSorteio": "Sorteio Aula 15",
    "numMin": 1,
    "numMax": 15
}
```

Este body passará o nome do sorteio como "Sorteio Aula 15" e sorteará um número aleatório entre 1 e 15.

4. **Salve** e **implante** a função.

Essa função receberá os números mínimo e máximo e retornará um número aleatório entre eles.

---

## **4. Integração com API Gateway**

### **O que é o API Gateway?**
O AWS API Gateway nos permite criar uma API REST para invocar a função Lambda a partir da página web.

#### **Passo a Passo: Configurando o API Gateway**

1. Acesse o **API Gateway** no console da AWS e crie uma nova API do tipo **REST API**.
2. Crie um método **POST** vinculado à função Lambda (`SorteioFunction`).
3. Copie a URL de invocação da API, que será usada no próximo passo para conectar o frontend ao backend.

---

## **5. Persistindo Dados no DynamoDB**

Agora que já temos a página de sorteio e a função Lambda configurada para realizar o sorteio, o próximo passo é armazenar os dados do sorteio no DynamoDB. Vamos criar uma tabela DynamoDB onde vamos salvar as seguintes informações:
- Nome do sorteio
- Número mínimo
- Número máximo
- Número sorteado

### **Passo a Passo: Criando a Tabela DynamoDB**

1. No console da AWS, vá até o serviço **DynamoDB** e clique em **Create Table**.
2. Defina o nome da tabela como `Sorteios`.
3. A chave de partição será `SorteioID` (tipo String).
4. Conclua a criação da tabela.

Agora, a tabela `Sorteios` está pronta para receber os dados dos sorteios.

---

## **6. Atualizando a Função Lambda para Persistir os Dados no DynamoDB**

Além de realizar o sorteio, agora a função Lambda vai salvar no DynamoDB o nome do sorteio, o intervalo de números (mínimo e máximo) e o número sorteado. Vamos atualizar a função Lambda para incluir essa lógica.

### **Passo a Passo: Atualizando a Função Lambda**

Atualize o código da sua função Lambda para persistir os dados no DynamoDB:

```python
import json
import random
import boto3
from time import gmtime, strftime

# Criar o objeto DynamoDB usando o SDK boto3
dynamodb = boto3.resource('dynamodb')
# Selecionar a tabela que criamos
table = dynamodb.Table('Sorteios')

# Função Lambda que realiza o sorteio e persiste os dados
def lambda_handler(event, context):
    nome_sorteio = event['nomeSorteio']
    num_min = int(event['numMin'])
    num_max = int(event['numMax'])
    numero_sorteado = random.randint(num_min, num_max)
    
    # Salvar os dados no DynamoDB
    response = table.put_item(
        Item={
            'SorteioID': strftime("%Y%m%d%H%M%S", gmtime()),  # Gerar um ID único baseado no horário
            'NomeSorteio': nome_sorteio,
            'NumeroMin': num_min,
            'NumeroMax': num_max,
            'NumeroSorteado': numero_sorteado,
            'DataSorteio': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())  # Data e hora do sorteio
        }
    )
    
    # Retornar o resultado do sorteio
    return {
        'statusCode': 200,
        'body': json.dumps({
            'nomeSorteio': nome_sorteio,
            'numeroSorteado': numero_sorteado
        })
    }
```

### **Explicação do Código:**
- **boto3**: Usamos o boto3 para interagir com o DynamoDB.
- **strftime**: Geramos um ID único para cada sorteio baseado na data e hora em que ele foi realizado.
- **put_item**: Salvamos os dados do sorteio (nome, números mínimo e máximo, número sorteado, e a data do sorteio) na tabela DynamoDB.

### **Atualizando o Frontend (Formulário HTML)**

### Aula Completa: Criando um Sistema de Sorteio com AWS e Frontend Integrado

Nesta aula, vamos implementar uma aplicação completa de sorteio, integrando frontend, AWS Lambda, DynamoDB e API Gateway. O usuário poderá inserir o nome do sorteio, o número mínimo e o número máximo. A função Lambda, acionada via API Gateway, retornará um número aleatório dentro desse intervalo e salvará os detalhes no DynamoDB.

---

### **7. Frontend: Página de Sorteio**

Vamos começar criando o frontend da nossa aplicação. Ele terá um formulário que captura os dados do sorteio e chama a API para realizar o sorteio.

#### **Código HTML do Frontend:**

Aqui está o código HTML para a página de sorteio. Vamos aplicar um design simples com tons de azul.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Sorteio Automático</title>
    <!-- Estilização da página -->
    <style>
    h1 {
        color: #FFFFFF;
        font-family: system-ui;
        margin-left: 20px;
    }
    body {
        background-color: #003366;
    }
    label {
        color: #66CCFF;
        font-family: system-ui;
        font-size: 20px;
        margin-left: 20px;
        margin-top: 20px;
    }
    button {
        background-color: #66CCFF;
        border-color: #66CCFF;
        color: #FFFFFF;
        font-family: system-ui;
        font-size: 20px;
        font-weight: bold;
        margin-left: 30px;
        margin-top: 20px;
        width: 140px;
    }
    input {
        color: #003366;
        font-family: system-ui;
        font-size: 20px;
        margin-left: 10px;
        margin-top: 20px;
        width: 100px;
    }
    </style>
    <script>
        // Função para chamar a API
        var realizarSorteio = (nomeSorteio, numMin, numMax) => {
            var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");

            var raw = JSON.stringify({
                "nomeSorteio": nomeSorteio,
                "numMin": numMin,
                "numMax": numMax
            });

            var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
                redirect: 'follow'
            };

            fetch("YOUR_API_GATEWAY_ENDPOINT", requestOptions)
            .then(response => response.text())
            .then(result => alert("Número sorteado: " + JSON.parse(result).numeroSorteado))
            .catch(error => console.log('error', error));
        }
    </script>
</head>
<body>
    <h1>Bem-vindo ao Sorteio Automático!</h1>
    <form>
        <label>Nome do sorteio:</label>
        <input type="text" id="nomeSorteio"><br>
        <label>Número Mínimo:</label>
        <input type="number" id="numMin"><br>
        <label>Número Máximo:</label>
        <input type="number" id="numMax"><br>
        <!-- Botão que chama a função realizarSorteio -->
        <button type="button" onclick="realizarSorteio(
            document.getElementById('nomeSorteio').value,
            document.getElementById('numMin').value,
            document.getElementById('numMax').value
        )">Realizar Sorteio</button>
    </form>
</body>
</html>
```