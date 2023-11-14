'''

Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.

'''

def pares():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    conjunto_pares = set()
    
    for numero in numeros:
        if numero % 2 == 0:
            conjunto_pares.add(numero)
            
    return conjunto_pares


def multiplos_de_tres():
    
    conjunto_multiplos_de_tres = set()
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    for numero in numeros:
        if numero % 3 == 0:
            conjunto_multiplos_de_tres.add(numero)
    
    return conjunto_multiplos_de_tres

def interseccion(numeros1,numeros2):
    
    interseccion = numeros1 & numeros2
    
    return interseccion
    
    
if __name__ == "__main__":
    
    
    numeros1 = pares()
    numeros2 = multiplos_de_tres()
    
    print(interseccion(numeros1,numeros2))
        