import requests

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main():
    urls = ["https://example.com"] * 10  # Lista de URLs para fetch
    responses = [fetch_url(url) for url in urls]
    for response in responses:
        print(response[:100])  # Printa os primeiros 100 caracteres de cada resposta

main()
