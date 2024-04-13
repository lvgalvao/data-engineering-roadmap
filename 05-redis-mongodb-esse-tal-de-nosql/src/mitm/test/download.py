import requests
from os import environ as env

# Configuração do proxy para o MITM Proxy
proxy = {
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080',
}

cert_path = './mitmproxy-ca-cert.pem'


# URL do arquivo que você deseja baixar
url = 'http://releases.ubuntu.com/22.04.4/ubuntu-22.04.4-desktop-amd64.iso'

headers = {
    # 'Proxy-Authorization': env.get("ARG1"),
    'Proxy-Authentication': env.get("ARG2"),
    # 'Proxy-Server' : '20.33.5.27:8888'
}

# Realiza a solicitação HTTP através do MITM Proxy
with requests.get(url, stream=True, proxies=proxy, verify=cert_path, headers=headers) as r:
# with requests.get(url, stream=True, proxies=proxy) as r:    
# Verifica o tamanho total do arquivo, se disponível
    total_size = r.headers.get('content-length')
    if total_size is None:
        print("O tamanho total do arquivo é desconhecido.")
    else:
        total_size = int(total_size)

    print(f'Tamanho do arquivo é {total_size}')
    # Inicializa a quantidade de bytes recebidos
    downloaded_size = 0

    # Trata a resposta conforme necessário
    if r.status_code == 200:
        with open('arquivo_baixado.iso', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # Verifica se há dados no chunk
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    if total_size:
                        progress = downloaded_size / total_size * 100
                        print(f"Progresso: {progress:.2f}%")
        print("Download concluído.")
    else:
        print(f"Erro: {r.status_code}")
