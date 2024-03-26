class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("A idade deve ser um número positivo.")

# Exemplo de uso
pessoa = Pessoa("João", 30)

# Usando o método getter para acessar o atributo 'nome'
print("Nome:", pessoa.nome)  # Saída: Nome: João

# Usando o método setter para alterar o atributo 'nome'
pessoa.nome = "Maria"
print("Novo nome:", pessoa.nome)  # Saída: Novo nome: Maria

# Usando o método get
