# Imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e o código para o container
COPY requirements.txt .
COPY app.py .

# Instala o Streamlit e outras dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define a porta padrão que o Streamlit usará
EXPOSE 80

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.enableCORS=false"]
