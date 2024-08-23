import os
from typing import List
import boto3
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Print para verificar se as variáveis de ambiente foram carregadas corretamente
print(f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print(f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")
print(f"AWS_REGION: {AWS_REGION}")
print(f"BUCKET_NAME: {BUCKET_NAME}")

# Configura o cliente S3
try:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    print("Cliente S3 configurado com sucesso.")
except Exception as e:
    print(f"Erro ao configurar o cliente S3: {e}")
    raise

def listar_arquivos(pasta: str) -> List[str]:
    """Lista todos os arquivos em uma pasta local."""
    arquivos: List[str] = []
    try:
        for nome_arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_completo):
                arquivos.append(caminho_completo)
        print(f"Arquivos listados na pasta '{pasta}': {arquivos}")
    except Exception as e:
        print(f"Erro ao listar arquivos na pasta '{pasta}': {e}")
        raise
    return arquivos

def upload_arquivos_para_s3(arquivos: List[str]) -> None:
    """Faz upload dos arquivos listados para o S3."""
    for arquivo in arquivos:
        nome_arquivo: str = os.path.basename(arquivo)
        try:
            print(f"Tentando fazer upload de '{nome_arquivo}' para o bucket '{BUCKET_NAME}'...")
            s3_client.upload_file(arquivo, BUCKET_NAME, nome_arquivo)
            print(f"{nome_arquivo} foi enviado para o S3.")
        except Exception as e:
            print(f"Erro ao enviar '{nome_arquivo}' para o S3: {e}")
            raise

def deletar_arquivos_locais(arquivos: List[str]) -> None:
    """Deleta os arquivos locais após o upload."""
    for arquivo in arquivos:
        try:
            os.remove(arquivo)
            print(f"{arquivo} foi deletado do local.")
        except Exception as e:
            print(f"Erro ao deletar o arquivo '{arquivo}': {e}")
            raise

def executar_backup(pasta: str) -> None:
    """Executa o processo completo de backup."""
    try:
        print(f"Iniciando o processo de backup para a pasta '{pasta}'...")
        arquivos: List[str] = listar_arquivos(pasta)
        if arquivos:
            upload_arquivos_para_s3(arquivos)
            deletar_arquivos_locais(arquivos)
        else:
            print("Nenhum arquivo encontrado para backup.")
    except Exception as e:
        print(f"Erro no processo de backup: {e}")
        raise

if __name__ == "__main__":
    PASTA_LOCAL: str = 'download'  # Substitua pelo caminho da sua pasta local
    try:
        executar_backup(PASTA_LOCAL)
    except Exception as e:
        print(f"Erro ao executar o backup: {e}")
