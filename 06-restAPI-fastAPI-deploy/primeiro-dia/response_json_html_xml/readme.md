https://medium.com/@denniskoko/implementing-content-negotiation-in-fastapi-371d03c59c02

Aceitar diferentes tipos de comunicação

### Exemplo com a API da NASA:

Para acessar a API da NASA, você precisa passar sua chave de API como um parâmetro na solicitação. Aqui está um exemplo usando cURL:

```bash
curl -X GET 'https://api.nasa.gov/planetary/apod?api_key=aJ87xjxneJaiBejYAfFrSSPJXR4Ce2RdMnlrYP3x' \
  -H 'Accept: application/json'
```

Neste exemplo, a chave da API (`api_key=aJ87xjxneJaiBejYAfFrSSPJXR4Ce2RdMnlrYP3x`) é passada como um parâmetro na URL.

### Exemplo com a API da Wikipedia:

A API da Wikipedia usa um método de autenticação diferente, onde você não precisa de uma chave de API, mas pode especificar o formato da resposta usando uma flag na solicitação. Aqui está um exemplo usando cURL:

```bash
curl -X GET 'https://en.wikipedia.org/w/api.php?action=query&format=xml&titles=Albert%20Einstein'
```

Neste exemplo, estamos fazendo uma solicitação para obter informações sobre "Albert Einstein" da Wikipedia. A flag `format=xml` é usada para especificar que queremos a resposta no formato XML.

### Diferença entre as duas APIs:

* A API da NASA requer uma chave de API para autenticação e utiliza o cabeçalho `Accept` para especificar o tipo de conteúdo desejado na resposta (JSON neste caso).
* A API da Wikipedia não requer uma chave de API, mas permite que você especifique o formato da resposta usando uma flag na própria URL da solicitação.


### API da NASA - Solicitação JSON:

```bash
# JSON
curl -X GET 'https://api.nasa.gov/planetary/apod?api_key=aJ87xjxneJaiBejYAfFrSSPJXR4Ce2RdMnlrYP3x' \
  -H 'Accept: application/json'
```

### API da NASA - Solicitação XML:

curl -X GET 'https://api.nasa.gov/planetary/apod' \                                                 
  -H 'Accept: application/xml'
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <error>
    <code>API_KEY_MISSING</code>
    <message>No api_key was supplied. Get one at https://api.nasa.gov:443</message>
  </error>
</response>%  


```bash
# XML
curl -X GET 'https://api.nasa.gov/planetary/apod?api_key=aJ87xjxneJaiBejYAfFrSSPJXR4Ce2RdMnlrYP3x' -H 'Accept: application/xml'
```

### API da Wikipedia - Solicitação JSON:

```bash
# JSON
curl -X GET 'https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Albert%20Einstein'
```

### API da Wikipedia - Solicitação XML:

```bash
# XML
curl -X GET 'https://en.wikipedia.org/w/api.php?action=query&format=xml&titles=Albert%20Einstein'
```

Esses exemplos demonstram como fazer solicitações para ambas as APIs especificando o formato da resposta desejada (JSON ou XML).


Aqui está um exemplo de como você pode usar o cURL para fazer solicitações para o endpoint `get_user_by_extension` com diferentes tipos de formato:

```bash
# Solicitar dados no formato JSON
curl -X GET 'http://localhost:8000/users?format=json'

# Solicitar dados no formato HTML
curl -X GET 'http://localhost:8000/users?format=html'

# Solicitar dados no formato XML
curl -X GET 'http://localhost:8000/users?format=xml'
```