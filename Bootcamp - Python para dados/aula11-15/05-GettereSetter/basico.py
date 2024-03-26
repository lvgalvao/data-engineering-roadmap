class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getter para o atributo 'nome'
    def get_nome(self):
        return self._nome

    # Setter para o atributo 'nome'
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para o atributo 'idade'
    def get_idade(self):
        return self._idade

    # Setter para o atributo 'idade'
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("A idade deve ser um número positivo.")

# Exemplo de uso
pessoa = Pessoa("João", 30)

# Usando o método getter para acessar o atributo 'nome'
print("Nome:", pessoa.get_nome())  # Saída: Nome: João

# Usando o método setter para alterar o atributo 'nome'
pessoa.set_nome("Maria")
print("Novo nome:", pessoa.get_nome())  # Saída: Novo nome: Maria

# Usando o método getter para acessar o atributo 'idade'
print("Idade:", pessoa.get_idade())  # Saída: Idade: 30

# Usando o método setter para alterar o atributo 'idade'
pessoa.set_idade(25)
print("Nova idade:", pessoa.get_idade())  # Saída: Nova idade: 25

# Tentando definir uma idade negativa
pessoa.set_idade(-5)  # Saída: A idade deve ser um número positivo.
