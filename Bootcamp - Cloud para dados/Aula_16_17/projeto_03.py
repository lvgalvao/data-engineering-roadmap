import streamlit as st
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de ambiente necessárias
client_id = os.environ['AZURE_CLIENT_ID']
tenant_id = os.environ['AZURE_TENANT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
storage_account_url = os.environ["AZURE_STORAGE_URL"]
container_name = "meucontainer"

# Configura credenciais usando Client Secret
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

# Função para upload de arquivo
def upload_file(file):
    try:
        blob_client = container_client.get_blob_client(file.name)
        blob_client.upload_blob(file, overwrite=True)
        st.success(f"Arquivo '{file.name}' enviado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao enviar arquivo: {str(e)}")

# Função para listar arquivos no container
def listar_arquivos():
    try:
        blobs = container_client.list_blobs()
        return [blob.name for blob in blobs]
    except Exception as e:
        st.error(f"Erro ao listar arquivos: {str(e)}")
        return []

# Interface do Streamlit
st.title("Upload para Azure Blob Storage")

uploaded_file = st.file_uploader("Escolha um arquivo para enviar", type=["csv", "txt", "png", "jpg", "pdf"])

if uploaded_file is not None:
    if st.button("Enviar"):
        upload_file(uploaded_file)

st.subheader("Arquivos no Container")
arquivos = listar_arquivos()
if arquivos:
    for arquivo in arquivos:
        st.write(f"- {arquivo}")
else:
    st.write("Nenhum arquivo encontrado.")
