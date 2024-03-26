import boto3
from botocore.exceptions import NoCredentialsError
import sys
import os

# Suponha que você tenha uma variável de ambiente chamada "MINHA_VARIAVEL"
# Você pode acessar seu valor usando a função os.environ.get()


class S3Client:

    def __init__(self):
        
        self._envs = {
            "aws_access_key_id": os.environ.get("AWS_ACCESS_KEY_ID"),
            "aws_secret_access_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
            "region_name": os.environ.get("AWS_REGION", "us-west-1"),  # Usando um valor padrão se a variável não estiver definida
            "s3_bucket": os.environ.get("S3_BUCKET_NAME"),
            "datalake" : os.environ.get("DELTA_LAKE_S3_PATH")
        }

        for var in self._envs:
            if self._envs[var] is None:
                print(f"A variável de ambiente {var} não está definida.")
                sys.exit(1)

        self.s3 = boto3.client('s3', aws_access_key_id=self._envs["aws_access_key_id"], aws_secret_access_key=self._envs["aws_secret_access_key"], region_name=self._envs["region_name"])

    def upload_file(self, data, s3_key):
        try:
            self.s3.put_object(Body=data.getvalue(), Bucket=self._envs["s3_bucket"], Key=s3_key)
        except NoCredentialsError:
            print("Credenciais não encontradas. Certifique-se de configurar suas credenciais AWS corretamente.")

    def download_file(self, s3_key):
        try:
            file = self.s3.get_object(Bucket=self._envs["s3_bucket"], Key=s3_key)
            print(f"Download bem-sucedido para {s3_key}")
            return file
        except NoCredentialsError:
            print("Credenciais não encontradas. Certifique-se de configurar suas credenciais AWS corretamente.")
        except FileNotFoundError:
            print(f"Arquivo {s3_key} não encontrado no bucket {self._envs['s3_bucket']}.")
        except Exception as e:
            print(f"Ocorreu um erro durante o download: {e}")

    def list_object(self, prefix):
        return self.s3.list_objects(Bucket=self._envs["s3_bucket"], Prefix=prefix)['Contents']