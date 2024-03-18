## Em Python, a sobrecarga de método não é diretamente suportada como em algumas outras linguagens de programação, 
## mas você pode simular sobrecarga usando parâmetros padrão ou argumentos variáveis.


class Calculadora:
    def soma(self, *args):
        total = 0
        for num in args:
            total += num
        return total

# Exemplo de uso
calculadora = Calculadora()
print(calculadora.soma(1, 2))        # Saída: 3
print(calculadora.soma(1, 2, 3, 4))  # Saída: 10
print(calculadora.soma(5, 10, 15))   # Saída: 30
