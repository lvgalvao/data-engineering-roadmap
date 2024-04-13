import requests
from os import environ as env

url = "http://lumtest.com/myip.json"
# url = "http://www.globo.com"

proxy = {
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080',
}

cert_path = './mitmproxy-ca-cert.pem'

headers = {
    'Proxy-Authorization': env.get("ARG1"),
    # 'x-New-Proxy-Auth': env.get("ARG2")
    # 'x-New-Proxy-Server' : '38.145.211.246:8899'
    # 'x-New-Proxy-Server' : 'No-Proxy'

}

# Fazendo a requisição GET
response = requests.get(url, proxies=proxy, verify=cert_path, headers=headers)
# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta (o endereço IP retornado pelo site)
    print("Endereço IP retornado pelo site:", response.json()["ip"])
    print("Cidade", response.json()["geo"] )
    
else:
    # Se a requisição não foi bem-sucedida, imprime o código de status
    print("Falha na requisição. Código de status:", response.status_code)