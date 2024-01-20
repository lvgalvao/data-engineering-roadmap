import pandas as pd
from contrato import UsuarioSchema

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Verifique se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(UsuarioSchema.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

        # Verifique se há as colunas do schema no DataFrame
        for index, row in df.iterrows():
            try:
                _ = UsuarioSchema(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")  # +2 porque o índice começa em 0 e a primeira linha do Excel é o cabeçalho

        return True, None

    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"