from azure.identity import ClientSecretCredential  # Importa a classe para autenticação usando Client Secret
from azure.keyvault.secrets import SecretClient  # Importa a classe para manipular segredos no Key Vault
from dotenv import load_dotenv  # Importa a função para carregar variáveis de ambiente de um arquivo .env
import os  # Importa o módulo para acessar variáveis de ambiente

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente necessárias para a autenticação
client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
vault_url = os.environ["AZURE_VAULT_URL"]

# Nome do segredo a ser acessado no Key Vault
secret_name = "ExemploKey"

# Cria uma credencial para autenticação no Azure utilizando Client Secret
credentials = ClientSecretCredential(
    client_id=client_id, 
    client_secret=client_secret,
    tenant_id=tenant_id
)

# Cria o cliente do Key Vault para acessar os segredos
secret_client = SecretClient(vault_url=vault_url, credential=credentials)

# Recupera o valor do segredo a partir do Key Vault
secret = secret_client.get_secret(secret_name)

# Exibe o valor do segredo no terminal
print("O valor do segredo é: " + secret.value)
