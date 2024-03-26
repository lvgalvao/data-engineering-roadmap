lista_de_numeros: list = [40,50,60,70,0,-408593,1,50]
lista_de_numeros_02: list = [40,60,70,0,-408593,1,50]
lista_de_numeros_03: list = [40,60,70,0,1,50]

# [40,50,60,70,0,-408593,1,50]
# [50,60,,700,-408593,1,50]

nome = "luciano"

def ordernar_lista(numeros: list) -> list:
    
    nova_lista_de_numeros = []
    
    try:
        nova_lista_de_numeros = numeros.copy()
        
        for i in range(len(nova_lista_de_numeros)):
            for j in range(i+1, len(nova_lista_de_numeros)):
                if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                    nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    
    except:
        print("Voce colocou uma str e ao inves de uma lista")
    
    return nova_lista_de_numeros

ordernar_lista(nome)