from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de ambiente necessárias
client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
storage_account_url = os.environ["AZURE_STORAGE_URL"]  # Ex: https://<nome_da_storage>.blob.core.windows.net/
container_name = "meucontainer"  # Nome do container criado

# Configura as credenciais usando Client Secret
credentials = ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id
)

# Conectar ao Blob Storage
blob_service_client = BlobServiceClient(
    account_url=storage_account_url,
    credential=credentials
)

# Acessa o container
container_client = blob_service_client.get_container_client(container_name)

# Lista todos os arquivos dentro do container
print(f"Listando arquivos no container '{container_name}':")
for blob in container_client.list_blobs():
    print(f" - {blob.name}")
