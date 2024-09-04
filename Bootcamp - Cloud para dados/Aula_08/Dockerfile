# Usar uma imagem base do Python
FROM python:3.12

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o container
COPY requirements.txt .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o conteúdo do projeto para o diretório de trabalho do container
COPY . .

# Comando para rodar o script fetch.py localizado na pasta src
CMD ["python", "src/fetch.py"]
