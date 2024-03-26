# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

# Solicita ao usuário que digite seu nome

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = "Luciano"

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif nome.isdigit():
            raise ValueError("O nome não deve conter números.") 
        else:
            nome_valido = True
            print("Nome válido:", nome)
    except ValueError as e:
        print(e)
# Solicita ao usuário 
# que digite o valor do seu salário e converte para float

while salario_valido is not True:
    try:
        salario = 2000
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
        
while bonus_valido is not True:        
    try:
        bonus = 3.0
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")