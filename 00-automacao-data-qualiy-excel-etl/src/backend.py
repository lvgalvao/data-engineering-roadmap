import pandas as pd
from contrato import UsuarioSchema

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        for _, row in df.iterrows():
            _ = UsuarioSchema(**row.to_dict())

        return True, None  # Processamento bem-sucedido

    except Exception as e:
        return False, str(e)  # Erro durante o processamento