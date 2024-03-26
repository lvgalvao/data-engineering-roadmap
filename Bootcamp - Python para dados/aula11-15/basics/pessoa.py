from datetime import datetime

def ola_Pessoa(pessoa):
    return f'Olá {pessoa["nome"]}'

def ano_nascimento_Pessoa(pessoa):
    ano_atual = datetime.now().year
    idade = int(pessoa["idade"])
    ano_nascimento = ano_atual - idade
    return f'você nasceu em: {ano_nascimento}'

def tem_emprego(pessoa):
    if pessoa["profissao"] == "Data Eng":
        return f'Não há vagas para: {pessoa["profissao"]}'
    
    return f'Vou te arranjar um emprego de {pessoa["profissao"]}'
        

pessoa = {
    "nome" : "Fabio",
    "idade" : "35",
    "profissao" : "Data Eng"
}

pessoa2 = {
    "nome" : "Luciano",
    "idade" : "33",
    "profissao" : "Data Product Manager"
}

print(pessoa)    
print(ola_Pessoa(pessoa))
print(ano_nascimento_Pessoa(pessoa))
print(tem_emprego(pessoa))

print(pessoa2)    
print(ola_Pessoa(pessoa2))
print(ano_nascimento_Pessoa(pessoa2))
print(tem_emprego(pessoa2))