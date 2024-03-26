from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def ola(self):
        return f'Olá {self.nome}'

    def ano_nascimento(self):
        ano_atual = datetime.now().year
        idade = int(self.idade)
        ano_nascimento = ano_atual - idade
        return f'Você nasceu em: {ano_nascimento}'

    def tem_emprego(self):
        if self.profissao == "Data Eng":
            return f'Não há vagas para: {self.profissao}'
        return f'Vou te arranjar um emprego de {self.profissao}'

# Exemplo de uso:
pessoa = Pessoa("Fabio", "35", "Data Eng")
pessoa2 = Pessoa("Luciano", "33", "Data Product Manager")
print(pessoa.ola())
print(pessoa.ano_nascimento())
print(pessoa.tem_emprego())

print(pessoa2.ola())
print(pessoa2.ano_nascimento())
print(pessoa2.tem_emprego())
