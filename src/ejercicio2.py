'''

Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, 
solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.

'''

def solicita():
    solicitar_primero=input("Ponga el nombre de los alumnos de primero (x para finalizar): ")
    primero = set()
    while solicitar_primero != 'x':
        primero.add(solicitar_primero)
        solicitar_primero=input("Ponga el nombre de los alumnos de primero (x para finalizar): ")
    solicitar_segundo = input("Ponga el nombre de los alumnos de segundo (x para finalizar): ")
    segundo = set()
    while solicitar_segundo != 'x':
        segundo.add(solicitar_segundo)
        solicitar_segundo = input("Ponga el nombre de los alumnos de segundo (x para finalizar): ")
    return primero, segundo

    
def sin_repeticion(conj1,conj2):
    sinrep = conj1 | conj2
    return sinrep

def con_repeticion(conj1,conj2):
    conrep = conj1 & conj2
    return conrep

def repeticon_primaria_secundaria(conj1,conj2):
    repprisec = conj1 - conj2
    return repprisec
    
def comunes(conj1,conj2):
    comparar = conj1 <= conj2
    return comparar


if __name__ == "__main__":
    
    alumnos = solicita()
    conj1 = alumnos[0]
    conj2 = alumnos[1]
    dato1= sin_repeticion(conj1,conj2)
    print('todos los alumnos sin repeticion:\n', dato1)
    dato2= con_repeticion(conj1,conj2)
    print('Los nombres repetidos son:\n', dato2)
    dato3= repeticon_primaria_secundaria(conj1,conj2)
    print('nombres de primaria no se repiten en los de nivel secundaria son:\n',dato3)
    dato4 = comunes(conj1,conj2)
    print(' nombres de primaria están incluidos en secundaria:\n', dato4)
    
    