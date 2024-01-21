import pandas as pd
from contrato import UsuarioSchema, VendasSchema, RecursosHumanosSchema

def process_excel(uploaded_file, model_name):
    """
    Processa um arquivo Excel, validando-o contra um esquema específico.

    Args:
        uploaded_file: Um arquivo Excel carregado pelo usuário.
        model_name: Nome do modelo de dados a ser usado para validação.

    Returns:
        Uma tupla (resultado, erro), onde 'resultado' é um booleano indicando se a validação
        foi bem-sucedida e 'erro' é uma mensagem de erro se a validação falhar.
    """    
    try:
        df = pd.read_excel(uploaded_file)

        # Escolher o schema correto com base em model_name
        if model_name == "Usuario":
            schema = UsuarioSchema
        elif model_name == "Vendas":
            schema = VendasSchema
        elif model_name == "Recursos Humanos":
            schema = RecursosHumanosSchema
        else:
            raise ValueError(f"Modelo desconhecido: {model_name}")

        # Verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(schema.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

        # Validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = schema(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")

        return True, None

    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"