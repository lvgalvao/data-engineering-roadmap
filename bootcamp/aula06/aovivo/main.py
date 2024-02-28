is_nome_aluno: int = 0

while is_nome_aluno is not True:
    nome_aluno = input("Digirw uma classe")
    if isinstance(nome_aluno, str):
        nome_aluno_maiusculo = nome_aluno.upper()
        print(nome_aluno_maiusculo)
        is_nome_aluno = True
    else:
        print("voce digitou uma classe errada, precisa ser str")
        is_nome_aluno = is_nome_aluno + 1
