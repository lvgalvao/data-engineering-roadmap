from pydantic import validate_call

@validate_call
def filtrar_acima_de(lista_de_salarios: list[float], salario_max: float) -> list:
    lista_de_salarios_acima: list = []
    for salario in lista_de_salarios:
        if salario > salario_max:
            lista_de_salarios_acima.append(salario)
    return lista_de_salarios_acima