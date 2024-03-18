import pandas as pd

from app.etl import transformar

def test_calculo_valor_total_estoque():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [10, 5],
        'preco': [20.0, 100.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series([200.0, 500.0], name='valor_total_estoque')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['valor_total_estoque'], expected)

def test_normalizacao_categoria():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [1, 2],
        'preco': [10.0, 20.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series(['BRINQUEDOS', 'ELETRÔNICOS'], name='categoria_normalizada')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['categoria_normalizada'], expected)

def test_determinacao_disponibilidade():
    # Preparação
    df = pd.DataFrame({
        'quantidade': [0, 2],
        'preco': [10.0, 20.0],
        'categoria': ['brinquedos', 'eletrônicos']
    })
    expected = pd.Series([False, True], name='disponibilidade')

    # Ação
    result = transformar(df)

    # Verificação
    pd.testing.assert_series_equal(result['disponibilidade'], expected)

# Para rodar os testes, execute `pytest nome_do_arquivo.py` no terminal.