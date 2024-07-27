import os  # Importação não utilizada
import sys  # Importação não utilizada

def function_one():
    pass

def function_two():
    pass

def example_function(a,b):  # Falta espaço após a vírgula
    """Exemplo de função com vários erros"""
    print("Esta é uma linha de código que é muito longa e ultrapassa o limite de 79 caracteres, o que não está de acordo com o PEP8.")  # Linha muito longa (E501)
    result = 1 \
        + 2  # Quebra de linha desnecessária (W503)
    myVariable = 10  # Nome de variável não está no estilo snake_case (N806)
    return result + a + b

def another_function():
    print(undefined_variable)  # Variável não definida (F821)

def function_with_trailing_whitespace():  
    pass  # Espaço em branco à direita (W291)

def function_without_docstring():
    pass  # Deveria ter uma docstring explicando a função (D103)

def function_with_missing_type_annotations(a, b):  # Deveria ter anotação de tipo (ANN001)
    return a + b

def unused_function_example():  # Função definida mas não utilizada (F841)
    pass

x = 5
y =  10  # Dois espaços antes da atribuição (E222)

def function_with_no_space_in_def(param1,param2):  # Falta de espaço após a vírgula (E231)
    return param1 + param2

def inconsistent_indentation():
  a = 5  # Indentação inconsistente (E111)
    b = 6
    return a + b

def mixed_tabs_and_spaces():
    a = 10  # Mistura de espaços e tabulações (E101)
	b = 20
	return a + b

def incorrect_default_argument(value=[]):  # Uso de lista mutável como valor padrão (B006)
    value.append(1)
    return value

def function_with_multiple_returns(a):  # Múltiplos retornos (C901)
    if a > 10:
        return True
    elif a == 10:
        return False
    else:
        return None

class ExampleClass:
    def __init__(self):
        self.value = 10  # Atributo não documentado (D107)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value  # Método setter sem validação (B008)
